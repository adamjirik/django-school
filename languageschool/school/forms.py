from django import forms
from django.contrib.auth.models import User
from django.forms import widgets, inlineformset_factory

from .models import Group, Student, Teacher, Classroom, Assignment, StudentAssignment

from django.contrib.auth.forms import UserCreationForm

class NewUserRegistration(UserCreationForm):
    CHOICES = (('s', 'Student'), ('t', 'Teacher'))
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    student_or_teacher = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class NewGroupForm(forms.ModelForm):
    group_name = forms.CharField()
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), widget=widgets.CheckboxSelectMultiple)
    language = forms.CharField()
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all())

    class Meta:
        model = Group
        fields = ['group_name', 'students', 'language', 'teacher', 'classroom']


class NewAssignmentForm(forms.ModelForm):

    description = forms.CharField(widget=widgets.Textarea)
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    due_date = forms.DateField(widget=widgets.SelectDateWidget)

    class Meta:
        model = Assignment

        fields = ['description', 'group', 'due_date']


    def save(self, commit=True):
        assignment = super().save(commit=False)
        assignment.description = self.cleaned_data['description']
        assignment.group = self.cleaned_data['group']
        assignment.due_date = self.cleaned_data['due_date']
        if commit:
            assignment.save()
            for student in assignment.group.students.all():
                student_assignment = StudentAssignment.objects.create(assignment=assignment, student=student)
                student_assignment.save()
        return assignment