from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

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
    students = models.ManyToManyField(Student)
    language = models.CharField(max_length=25)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s" % (self.group_name)

class Assignment(models.Model):
    description = models.TextField(max_length=80)
    due_date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='StudentAssignment')


class StudentAssignment(models.Model):
    student = models.ForeignKey(Student, related_name='students', db_column='student_id', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, db_column='assignment_id', on_delete=models.CASCADE)
    grade = models.FloatField(default=0.01)


