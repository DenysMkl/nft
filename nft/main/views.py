from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *
from .forms import RegisterUserForm, AuthUserForm, Customer_images_form, Customer_data_form


def index(req):
    acc_images, acc_info = None, None

    if req.user.is_authenticated:

        if not Customer_images.objects.filter(customer_name=req.user):
            Customer_images.objects.create(customer_name=req.user)

        if not Customer_data.objects.filter(customer_name=req.user):
            Customer_data.objects.create(customer_name=req.user)

        acc_images = Customer_images.objects.get(customer_name=req.user)
        acc_info = Customer_data.objects.get(customer_name=req.user)

    return render(req, 'main/index.html', context={'isMainPage': True, 'acc_images': acc_images, 'acc_info': acc_info})

@login_required
def createNFT(req):
    acc_images = Customer_images.objects.get(customer_name=req.user)
    acc_info = Customer_data.objects.get(customer_name=req.user)
    return render(req, 'main/create-NFT.html', context={'acc_images': acc_images, 'acc_info': acc_info})

@login_required
def profile(req):
    acc_images = Customer_images.objects.get(customer_name=req.user)
    acc_info = Customer_data.objects.get(customer_name=req.user)
    return render(req, 'main/user-page.html', context={'acc_images': acc_images, 'acc_info': acc_info})


@login_required
def settings(req):
    form = Customer_images_form()
    data = Customer_data_form()

    acc_images = Customer_images.objects.get(customer_name=req.user)
    acc_info = Customer_data.objects.get(customer_name=req.user)
    for i in data:
        i.initial = getattr(acc_info, f'{i.name}')


    if req.method == 'POST':
        mass_of_data = req.POST
        forma = Customer_images_form(req.POST, req.FILES, instance=acc_images) if 'detect' in mass_of_data else Customer_data_form(req.POST, instance=acc_info)

        if forma.is_valid():
            forma.save()
            return redirect('sett')
    else:
        forma = Customer_images()

    return render(req, 'main/profile-page.html', context={'acc_images': acc_images, 'form': form, 'data_form': data, 'acc_info': acc_info})

@login_required
def prod_page(req):

    acc_images = Customer_images.objects.get(customer_name=req.user)
    acc_info = Customer_data.objects.get(customer_name=req.user)
    return render(req, 'main/goods-temp.html', context={'acc_images': acc_images, 'acc_info': acc_info})


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

def profiles(req, value):
    acc_info = get_object_or_404(Customer_data, user_name=f'@{value}')
    acc_images = Customer_images.objects.get(customer_name=acc_info.customer_name)


    return render(req, 'main/user-page.html', context={'acc_images': acc_images, 'acc_info': acc_info})
