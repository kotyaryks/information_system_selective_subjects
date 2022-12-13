"""selective_subjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from inform_sys_selective_subjects import views as infosys
from uni_structure import views as user

urlpatterns = [
    path('adminsite/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('login/', user.user_login, name='login'),
    path('logout/', user.user_logout, name='logout'),
    path('profile/', user.user_profile, name='profile'),
    path('registration/', user.user_register, name='register'),
    path('registration/next/', user.student_register, name='register_next'),
    path('', infosys.home, name='home'),
    path('uni_subjects_list/', infosys.uni_subjects_list, name='uni_subjects_list'),
    path('faculty_list/', infosys.faculty_list, name='faculty_list'),
    path('faculty_subjects_list/<int:faculty_id>/', infosys.faculty_subjects_list, name='faculty_subjects_list'),
    path('subject/', infosys.subject, name='subject'),
    path('subject_view/<int:subject_id>/', infosys.subject_view, name='subject_view'),
]
