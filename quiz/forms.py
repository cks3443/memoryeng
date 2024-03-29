from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']