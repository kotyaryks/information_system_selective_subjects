from django.contrib import admin

from .models import Faculty, Department, Majoring, Semester, AcademicYear

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Majoring)
admin.site.register(Semester)
admin.site.register(AcademicYear)
