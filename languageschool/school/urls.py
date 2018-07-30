from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('classrooms/', views.ClassroomListView.as_view(), name='classroom-list'),
	path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
	path('groups/', views.GroupListView.as_view(), name='group-list'),
	path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group-detail'),
	path('groups/add/', views.GroupCreateView.as_view(), name='group-add'),
	path('logout/', views.logout, {'next_page': ''}, name='logout'),
]