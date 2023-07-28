from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *
from .forms import RegisterUserForm, AuthUserForm, Customer_images_form, Customer_data_form


def index(req):
    prof = None

    if req.user.is_authenticated:

        if not Customer_images.objects.filter(customer_name=req.user):
            Customer_images.objects.create(customer_name=req.user)

        if not Customer_data.objects.filter(customer_name=req.user):
            Customer_data.objects.create(customer_name=req.user)

        prof = Customer_images.objects.get(customer_name=req.user)

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
    data = Customer_data_form()

    prof = Customer_images.objects.get(customer_name=req.user)
    prof_data = Customer_data.objects.get(customer_name=req.user)
    for i in data:
        i.initial = getattr(prof_data, f'{i.name}')


    if req.method == 'POST':
        mass_of_data = req.POST
        forma = Customer_images_form(req.POST, req.FILES, instance=prof) if 'detect' in mass_of_data else Customer_data_form(req.POST, instance=prof_data)

        if forma.is_valid():
            forma.save()
            return redirect('sett')
    else:
        forma = Customer_images()

    return render(req, 'main/profile-page.html', context={'accs': prof, 'form': form, 'data_form': data})


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