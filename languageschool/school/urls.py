from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('classrooms/', views.ClassroomListView.as_view(), name='classroom-list'),
	path('classrooms/<int:pk>', views.ClassroomDetailView.as_view(), name='classroom-detail'),
	path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
	path('groups/', views.GroupListView.as_view(), name='group-list'),
	path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group-detail'),
	path('groups/add/', views.GroupCreateView.as_view(), name='group-add'),
	path('logout/', views.logout, {'next_page': '/'}, name='logout'),
	path('assignments/', views.AssignmentListView.as_view(), name='assignment-list'),
	path('assignments/<int:pk>', views.AssignmentDetailView.as_view(), name='assignment-detail'),
	path('assignments/add/', views.AssignmentCreateView.as_view(), name='assignment-add')
]