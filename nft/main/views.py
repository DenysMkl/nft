from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *
from .forms import RegisterUserForm, AuthUserForm



def index(req):
    items = Customer_images.objects.all()
    return render(req, 'main/index.html', context={'isMainPage': True, 'accs': items})


def createNFT(req):
    items = Customer_images.objects.all()
    return render(req, 'main/create-NFT.html', context={'accs': items})


def profile(req):
    items = Customer_images.objects.all()
    return render(req, 'main/user-page.html', context={'accs': items})
@login_required
def settings(req):
    items = Customer_images.objects.all()
    return render(req, 'main/profile-page.html', context={'accs': items})


def prod_page(req):
    items = Customer_images.objects.all()
    return render(req, 'main/goods-temp.html', context={'accs': items})


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('auth')

class Auth(LoginView):
    form_class = AuthUserForm
    template_name = 'main/auth.html'

    def get_success_url(self):
            return reverse_lazy('main')

def logout_user(req):
    logout(req)
    return redirect('main')