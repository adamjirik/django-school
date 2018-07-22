from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class NewUserRegistration(UserCreationForm):
    CHOICES = (('s', 'Student'), ('t', 'Teacher'))
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    student_or_teacher = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
