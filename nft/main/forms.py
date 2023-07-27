from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='full name', widget=forms.TextInput(attrs={'class': 'inputTag', 'id': 'fullName'}))
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'class': 'inputTag', 'id': 'email'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'inputTag pass', 'id': 'pass'}))
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class': 'inputTag pass repeat', 'id': 'repeatpass'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthUserForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'inputTag', 'id': 'fullName'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'inputTag pass', 'id': 'pass'}))
