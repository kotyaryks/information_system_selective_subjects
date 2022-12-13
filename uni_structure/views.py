from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

from info_sys_users.models import Student, Lecturer
from inform_sys_selective_subjects.models import SelectedSubjectsByStudentList, Subject
from uni_structure.forms import LoginForm, StudentForm
from uni_structure.models import Majoring


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['email'],
                password=cd['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(
                    request,
                    ("Помилка авторизації, спробуйте ще")
                )
                return redirect('login')
    else:
        form = LoginForm()

    template = loader.get_template('inform_sys_selective_subjects/login.html')
    return HttpResponse(template.render({'form': form}, request))


def user_logout(request):
    logout(request)
    return redirect('home')


def user_profile(request):
    if Student.objects.filter(user_id=request.user.id):
        try:
            student = Student.objects.get(user_id=request.user.id)
            selected_subjects_list = SelectedSubjectsByStudentList.objects.order_by('students_id')
            email = request.user.username
            context = {
                'student': student,
                'selected_subjects_list': selected_subjects_list,
                'email': email,
            }
            template = loader.get_template('inform_sys_selective_subjects/student_profile.html')
        except Student.DoesNotExist:
            pass
    elif Lecturer.objects.filter(user_id=request.user.id):
        try:
            lecturer = Lecturer.objects.get(user_id=request.user.id)
            subjects_list = Subject.objects.filter(lecturer=lecturer)
            context = {
                'lecturer': lecturer,
                'subjects_list': subjects_list,
            }
            template = loader.get_template('inform_sys_selective_subjects/lecturer_profile.html')
        except Lecturer.DoesNotExist:
            pass

    else:
        return redirect('register_next')
    return HttpResponse(template.render(context, request))


def user_register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Success"))
            return redirect('register_next')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserCreationForm()

    return render(request, 'inform_sys_selective_subjects/registration.html', {
        'user_form': user_form,
    })


@csrf_exempt
def student_register(request):
    if request.method == 'POST':
        user_form = StudentForm(request.POST)
        if user_form.is_valid():
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            patronymic = user_form.cleaned_data['patronymic']
            majoring = user_form.cleaned_data['majoring']
            level = user_form.cleaned_data['level']

            user = Student.objects.create(
                user_id=request.user.id,
                first_name=first_name,
                last_name=last_name,
                patronymic=patronymic,
                majoring_id=majoring.id,
                level=level
            )
            messages.success(request, ("Success"))
            return redirect('register_next')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = StudentForm()
        majorings_list = Majoring.objects.all()
        context = {
            'user_form': user_form,
            'majorings_list': majorings_list,
        }

    return render(request, 'inform_sys_selective_subjects/register_next.html', context)
