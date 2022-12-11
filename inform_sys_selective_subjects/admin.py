from django.contrib import admin

from .models import Subject, SelectedSubjectsByStudentList


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['name', ]


@admin.register(SelectedSubjectsByStudentList)
class SelectedSubjectsByStudentListAdmin(admin.ModelAdmin):
    search_fields = ['students', ]

# Register your models here.
