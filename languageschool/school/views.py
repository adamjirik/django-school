from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserRegistration
from .models import Student, Teacher

# Create your views here.
def index(request):
    return render(request, 'content.html')

def register(request):
    if request.method == 'POST':
        form = NewUserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password,
                                first_name=first_name, last_name= last_name, email=email)
            if form.cleaned_data.get('student_or_teacher') == 's':
                new_student = Student.objects.create(user=user)
                new_student.save()
            elif form.cleaned_data.get('student_or_teacher') == 't':
                new_teacher = Teacher.objects.create(user=user)
                new_teacher.save()
            login(request, user)
            return redirect('index')
    else:
        form = NewUserRegistration()
    return render(request, 'register.html', {'form': form})