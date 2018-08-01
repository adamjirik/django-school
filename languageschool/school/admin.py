from django.contrib import admin
from .models import Student, Teacher, Group, SchoolLesson
# Register your models here.


class SchoolLessonAdmin(admin.ModelAdmin):
    list_display = ['group', 'classroom', 'day_of_the_week', 'start_time', 'end_time']


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(SchoolLesson)