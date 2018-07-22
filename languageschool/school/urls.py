from django.urls import path

from .views import index, register, ClassroomListView, TeacherListView

urlpatterns = [
	path('', index, name='index'),
	path('register/', register, name='register'),
	path('classrooms/', ClassroomListView.as_view()),
	path('teachers/', TeacherListView.as_view())
]