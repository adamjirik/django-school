from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout
from .forms import NewUserRegistration, NewGroupForm, NewAssignmentForm
from .models import Student, Teacher, Classroom, Group, Assignment, StudentAssignment
from django.views.generic import ListView, DetailView, CreateView, FormView

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
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            # email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
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

def logoout_view(request):
    logout(request)


class ClassroomListView(ListView):
    model = Classroom
    context_object_name = 'classroom_list'




class ClassroomDetailView(DetailView):
    model = Classroom
    context_object_name = 'classroom'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.get_object().schoollesson_set.all()
        return context


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'

class GroupListView(ListView):
    model = Group
    context_object_name = 'group_list'

class GroupDetailView(DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_list'] = self.get_object().students.all()
        return context

class GroupCreateView(CreateView):
    model = Group
    form_class = NewGroupForm

class AssignmentListView(ListView):
    model = Assignment
    context_object_name = 'assignment_list'

class AssignmentDetailView(DetailView):
    model = Assignment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_assignments'] = StudentAssignment.objects.filter(assignment=self.get_object())
        return context

class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = NewAssignmentForm

