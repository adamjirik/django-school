from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.


########################################
# Abstract User model
########################################
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)



########################################
#
########################################


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assignments = models.ManyToManyField('Assignment', through='StudentAssignment')

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Classroom(models.Model):
    room_name = models.CharField(max_length=15)
    seats = models.IntegerField()

    def __str__(self):
        return "%s" % (self.room_name)

class Group(models.Model):
    group_name = models.CharField(max_length=10)
    slug = models.SlugField()
    students = models.ManyToManyField(Student)
    language = models.CharField(max_length=25)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s" % (self.group_name)


    ########################################
    # Assignments
    ########################################

class Assignment(models.Model):
    description = models.TextField(max_length=80)
    due_date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='StudentAssignment')

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'slug': self.group.slug})


class StudentAssignment(models.Model):
    student = models.ForeignKey(Student, related_name='students', db_column='student_id', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, db_column='assignment_id', on_delete=models.CASCADE)
    grade = models.FloatField(default=0.01)

    ########################################
    # Lessons
    ########################################

DAYS_OF_THE_WEEK = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),

)

class SchoolLesson(models.Model):


    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    days_of_week = models.CharField(max_length=1, choices=DAYS_OF_THE_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = 'Lessons'
        verbose_name_plural = 'Lessons'
        ordering = ['days_of_week', 'start_time']

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (
                new_end >= fixed_start and new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        lessons = SchoolLesson.objects.filter(days_of_week=self.days_of_week)
        if lessons.exists():
            for lesson in lessons:
                if self.check_overlap(lesson.start_time, lesson.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another lesson: ' + str(lesson.days_of_week) + ', ' + str(
                            lesson.start_time) + '-' + str(lesson.end_time))