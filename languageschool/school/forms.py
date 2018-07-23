from django import forms
from django.contrib.auth.models import User

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

