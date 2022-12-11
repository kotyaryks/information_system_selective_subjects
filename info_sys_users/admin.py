from django.contrib import admin
from .models import Student, Lecturer


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'patronymic']
    list_filter = ['majoring', 'level']


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'patronymic']
    list_filter = ['department']
