from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='full name', widget=forms.TextInput(attrs={'class': 'inputTag', 'id': 'fullName'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class': 'inputTag', 'id': 'email'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'inputTag pass', 'id': 'pass'}))
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class': 'inputTag pass repeat', 'id': 'repeatpass'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthUserForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'inputTag', 'id': 'fullName'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'inputTag pass', 'id': 'pass'}))


class Customer_images_form(forms.ModelForm):
    class Meta:
        model = Customer_images
        fields = ('customer_bg', 'customer_avatar')
        widgets = {
            'customer_avatar': forms.FileInput(attrs={'id': 'user-avatar'}),
            'customer_bg': forms.FileInput(attrs={'id': 'user-bg'})
        }


class Customer_data_form(forms.ModelForm):

    class Meta:
        model = Customer_data
        fields = ('full_name', 'user_name', 'inst_link', 'tg_link', 'descr')
        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'inp-full-name'}),
            'user_name': forms.TextInput(attrs={'id': 'inp-user-name'}),
            'inst_link': forms.TextInput(attrs={'id': 'inp-inst'}),
            'tg_link': forms.TextInput(attrs={'id': 'inp-tg'}),
            'descr': forms.Textarea(attrs={'id': 'user-bio', 'placeholder': "Say something about yourself"})
        }
        labels = {
            'full_name': 'full name',
            'user_name': 'user name',
            'inst_link': 'instagram',
            'tg_link': 'telegram',
            'descr': 'description'
        }