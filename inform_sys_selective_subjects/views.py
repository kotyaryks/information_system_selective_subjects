from django.http import HttpResponse
from django.template import loader

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

def subject_view(request,subject_id):
    subject = Subject.objects.get(id=subject_id)
    context = {
        'subject': subject,
    }
    template = loader.get_template('inform_sys_selective_subjects/subject_view.html')
    return HttpResponse(template.render(context, request))


def uni_subjects_list(request):
    subjects = Subject.objects.all()#get(part='u')
    context = {
        'subjects_list': subjects,
    }
    template = loader.get_template('inform_sys_selective_subjects/uni_subjects_list.html')
    return HttpResponse(template.render(context, request))