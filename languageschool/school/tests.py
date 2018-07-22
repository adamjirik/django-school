from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from .models import Student, Group, Classroom, Teacher, Assignment, StudentAssignment
from django.contrib.auth.models import User
import datetime

# Create your tests here.

class ModelTest(TestCase):

    def test_can_make_a_group_with_teacher_student_classroom(self):
        user1 = User.objects.create(username='test', password='123')
        user2 = User.objects.create(username='test2', password='123')
        user1.save()
        user2.save()

        st = Student.objects.create(user = user1)
        te = Teacher.objects.create(user = user2)
        st.save()
        te.save()

        classroom = Classroom.objects.create(room_name = 'test class', seats = 4)

        classroom.save()

        group = Group.objects.create(language = 'spanish', group_name = 'group test', classroom = classroom, teacher = te)
        group.save()
        group.students.add(st)

class AssignmentTest(TestCase):
    def test_assignment_can_give_grades_to_different_students(self):
        user1 = User.objects.create(username='test', password='123')
        user2 = User.objects.create(username='test2', password='123')
        user3 = User.objects.create(username='test3', password='123')
        st = Student.objects.create(user=user1)
        st2 = Student.objects.create(user=user2)
        te = Teacher.objects.create(user=user3)
        st.save()
        st2.save()
        te.save()

        classroom = Classroom.objects.create(room_name='test class', seats=4)
        classroom.save()

        group = Group.objects.create(language='spanish', group_name='group test', classroom=classroom, teacher=te)
        group.save()
        group.students.set([st, st2])

        assign = Assignment.objects.create(description='test',due_date=datetime.datetime.now(), group=group)
        assign2 = Assignment.objects.create(description='test2',due_date=datetime.datetime.now(), group=group)
        grade = StudentAssignment(student = st, assignment=assign, grade=99.9)
        grade2 = StudentAssignment(student = st2, assignment=assign, grade=88.8)
        grade3 = StudentAssignment(student= st, assignment = assign2, grade = 80.0)
        grade.save()
        grade2.save()
        grade3.save()
        assign_students = assign.students.all()
        self.assertIn(st, assign_students)
        self.assertIn(st2, assign_students)
        st_assignments = StudentAssignment.objects.filter(student=st)
        st_grades = []
        for assignment in st_assignments:
            st_grades.append(assignment.grade)
        self.assertIn(80.0, st_grades)

class NewUserTest(TestCase):
    def test_user_has_full_info_and_is_related_to_student_or_teacher(self):
        pass