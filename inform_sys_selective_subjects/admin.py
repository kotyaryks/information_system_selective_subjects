from django.contrib import admin

from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['name',]
# Register your models here.
