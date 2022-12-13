from django.http import HttpResponse
from django.template import loader

from uni_structure.models import Department, Faculty, Majoring
from .models import Subject


def home(request):
    subjects = Subject.objects.all()
    context = {
        'subjects_list': subjects,
    }
    template = loader.get_template('inform_sys_selective_subjects/index.html')
    return HttpResponse(template.render(context, request))


def subject(request):
    subjects = Subject.objects.all()
    context = {
        'subjects_list': subjects,
    }
    template = loader.get_template('inform_sys_selective_subjects/subject.html')
    return HttpResponse(template.render(context, request))


def subject_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    context = {
        'subject': subject,
    }
    template = loader.get_template('inform_sys_selective_subjects/subject_view.html')
    return HttpResponse(template.render(context, request))


def uni_subjects_list(request):
    subjects = Subject.objects.filter(part='u').order_by('department')

    department_list = []
    for subject in subjects:
        if subject.department not in department_list:
            department_list.append(subject.department)

    faculty_list = []
    for department in department_list:
        if department.faculty not in faculty_list:
            faculty_list.append(department.faculty)

    context = {
        'faculty_list': faculty_list,
        'department_list': department_list,
        'subjects_list': subjects,
    }
    template = loader.get_template('inform_sys_selective_subjects/uni_subjects_list.html')
    return HttpResponse(template.render(context, request))


def faculty_list(request):
    faculty_list = Faculty.objects.all()
    context = {
        'faculty_list': faculty_list,
    }
    template = loader.get_template('inform_sys_selective_subjects/faculty_list.html')
    return HttpResponse(template.render(context, request))


def faculty_subjects_list(request, faculty_id):
    departments = Department.objects.filter(faculty_id=faculty_id)
    print(departments)

    subjects_list = []

    for department in departments:
        subjects_list.append(Subject.objects.filter(part='f').filter(department_id=department.id))

    print(subjects_list)

    majorings_list = []

    for department in departments:
        majorings_list.append(Majoring.objects.filter(department_id=department.id))

    print(majorings_list)

    context = {
        'majorings_list': majorings_list,
        'department_list': departments,
        'subjects_list': subjects_list,
        'faculty_id': faculty_id,
    }
    template = loader.get_template('inform_sys_selective_subjects/faculty_subjects_list.html')
    return HttpResponse(template.render(context, request))
