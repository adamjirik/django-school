from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	# path('register/', views.register, name='register'),
	path('classrooms/', views.ClassroomListView.as_view(), name='classroom-list'),
	path('classrooms/<int:pk>', views.ClassroomDetailView.as_view(), name='classroom-detail'),
	path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
	path('groups/', views.GroupListView.as_view(), name='group-list'),
	path('groups/add/', views.GroupCreateView.as_view(), name='group-add'),
	path('groups/<slug:slug>/', views.GroupDetailView.as_view(), name='group-detail'),
	path('groups/<slug:slug>/assignments/add/', views.AssignmentCreateView.as_view(), name='assignment-add'),
	path('groups/<slug:slug>/assignments/', views.AssignmentListView.as_view(), name='assignment-list'),
	path('groups/<slug:slug>/assignments/<int:pk>', views.AssignmentDetailView.as_view(), name='assignment-detail'),
	path('logout/', views.logout, {'next_page': '/'}, name='logout'),
]

