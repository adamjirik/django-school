from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Person(models.Model):
#
#     first_name = models.TextField(max_length=50)
#     last_name = models.TextField(max_length=50)
#
#     class Meta:
#         abstract = True

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Classroom(models.Model):
    room_name = models.TextField(max_length=15)
    seats = models.IntegerField()

class Group(models.Model):
    group_name = models.TextField(max_length=10)
    students = models.ManyToManyField(Student)
    language = models.TextField()
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


class Assignment(models.Model):
    description = models.TextField(max_length=80)
    due_date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='StudentAssignment')


class StudentAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.FloatField()
