from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

from django import forms

from info_sys_users.models import Student


class LoginForm(forms.Form):
    email = forms.CharField(label="", widget=forms.EmailInput)
    password = forms.CharField(label="",
                               widget=forms.PasswordInput)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'patronymic', 'majoring','level')
