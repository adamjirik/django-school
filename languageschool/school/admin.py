from django.contrib import admin
from .models import Student, Teacher, Group, SchoolLesson
# Register your models here.


class SchoolLessonAdmin(admin.ModelAdmin):
    list_display = ['group', 'classroom', 'day_of_the_week', 'start_time', 'end_time']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'slug', 'language', 'teacher', 'classroom']
    prepopulated_fields = {"slug": ("group_name",)}


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group, GroupAdmin)
admin.site.register(SchoolLesson)