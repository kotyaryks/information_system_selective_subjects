from django.contrib import admin

from .models import Subject, SelectedSubjectsByStudentList


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    filter_horizontal = ['majoring','lecturer','semester']


@admin.register(SelectedSubjectsByStudentList)
class SelectedSubjectsByStudentListAdmin(admin.ModelAdmin):
    search_fields = ['students', ]
    list_filter = ['subjects','academic_year',]

# Register your models here.
