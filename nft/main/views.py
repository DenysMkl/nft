from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *
from .forms import RegisterUserForm, AuthUserForm, Customer_images_form


def index(req):
    prof = Customer_images.objects.get(customer_name=req.user)

    if req.user.is_authenticated and not Customer_images.objects.filter(customer_name=req.user):
        Customer_images.objects.create(customer_name=req.user)
    return render(req, 'main/index.html', context={'isMainPage': True, 'accs': prof})


def createNFT(req):
    prof = Customer_images.objects.get(customer_name=req.user)
    return render(req, 'main/create-NFT.html', context={'accs': prof})


def profile(req):
    prof = Customer_images.objects.get(customer_name=req.user)
    return render(req, 'main/user-page.html', context={'accs': prof})
@login_required
def settings(req):
    form = Customer_images_form()
    prof = Customer_images.objects.get(customer_name=req.user)

    if req.method == 'POST':
        forma = Customer_images_form(req.POST, req.FILES, instance=prof)
        if forma.is_valid():
            forma.save()
            return redirect('sett')
    else:
        forma = Customer_images()

    return render(req, 'main/profile-page.html', context={'accs': prof, 'form': form})


def prod_page(req):

    prof = Customer_images.objects.get(customer_name=req.user)
    return render(req, 'main/goods-temp.html', context={'accs': prof})


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