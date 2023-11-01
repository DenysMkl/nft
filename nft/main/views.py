import json
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from .models import *
from .forms import RegisterUserForm, AuthUserForm, Customer_images_form, Customer_data_form, AddProduct


def get_all():
    return Customer_data.objects.all()


def define(req):
    account_images = Customer_images.objects.get(customer_name=req.user)
    account_info = Customer_data.objects.get(customer_name=req.user)
    return account_images, account_info


def index(req):
    acc_images, acc_info = None, None

    if req.user.is_authenticated:

        if not Customer_images.objects.filter(customer_name=req.user):
            Customer_images.objects.create(customer_name=req.user)

        if not Customer_data.objects.filter(customer_name=req.user):
            Customer_data.objects.create(customer_name=req.user)

        acc_images, acc_info = define(req)
    return render(req, 'main/index.html', context={'isMainPage': True,
                                                   'acc_images': acc_images,
                                                   'acc_info': acc_info})


@login_required
def createNFT(req):
    acc_images, acc_info = define(req)
    form = AddProduct()

    if req.method == 'POST':
        fill_form = AddProduct(req.POST)
        if fill_form.is_valid():
            fill_form.save()
            return redirect('nftcr')
        else:
            print(fill_form.errors)
    return render(req, 'main/create-NFT.html', context={'acc_images': acc_images,
                                                        'acc_info': acc_info,
                                                        'form': form})


@login_required
def settings(req):
    img_form = Customer_images_form()
    acc_images, acc_info = define(req)
    data_form = Customer_data_form()
    for i in data_form:
        i.initial = getattr(acc_info, f'{i.name}')

    if req.method == 'POST':

        images_fill_form = Customer_images_form(req.POST, req.FILES, instance=acc_images)
        data_fill_form = Customer_data_form(req.POST, instance=acc_info)
        forma = images_fill_form if 'detect' in req.POST else data_fill_form
        
        if forma.is_valid():
            forma.save()
            return redirect('sett')
    else:
        forma = Customer_images()

    return render(req, 'main/profile-page.html', context={'acc_images': acc_images,
                                                          'img_form': img_form,
                                                          'data_form': data_form,
                                                          'acc_info': acc_info})


@login_required
def prod_page(req):
    acc_images, acc_info = define(req)
    return render(req, 'main/goods-temp.html', context={'acc_images': acc_images,
                                                        'acc_info': acc_info})


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


@csrf_exempt
def api_view(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        user_acc = Customer_data.objects.get(user_name=f"{data['user_name']}")
        data_about_users_followers = Follower.objects.filter(follower=user_acc.customer_name)
        data_about_users_followings = Follower.objects.filter(owner_of_acc=user_acc.customer_name)

        followers_data = [Customer_data.objects.values().get(customer_name=i.follower) for i in
                          data_about_users_followings]
        followings_data = [Customer_data.objects.values().get(customer_name=i.owner_of_acc) for i in
                           data_about_users_followers]
        followers_imgs = [Customer_images.objects.values('customer_avatar').get(customer_name=i.follower) for i in
                          data_about_users_followings]
        followings_imgs = [Customer_images.objects.values('customer_avatar').get(customer_name=i.owner_of_acc) for i in
                           data_about_users_followers]

        return JsonResponse(
            {'followers': [followers_data, followers_imgs], 'followings': [followings_data, followings_imgs]})


@login_required
@csrf_exempt
def profiles(req, value):
    visit_acc_info = get_object_or_404(Customer_data, user_name=f'{value}')
    visit_acc_images = Customer_images.objects.get(customer_name=visit_acc_info.customer_name)
    acc_images, acc_info = define(req)
    isFollowed = bool(
        Follower.objects.filter(follower=acc_info.customer_name, owner_of_acc=visit_acc_info.customer_name))
    list_of_followers = Follower.objects.filter(owner_of_acc=visit_acc_info.customer_name)
    list_of_followings = Follower.objects.filter(follower=visit_acc_info.customer_name)
    if req.method == 'POST':
        data = json.loads(req.body)
        if data['process'] == 'follow':
            Follower.objects.create(follower=acc_info.customer_name, owner_of_acc=visit_acc_info.customer_name)
            return JsonResponse({'followers_count': len(list_of_followers)}, status=201)
        elif data['process'] == 'unfollow':
            Follower.objects.get(follower=acc_info.customer_name, owner_of_acc=visit_acc_info.customer_name).delete()
            return JsonResponse({'followers_count': len(list_of_followers)})

    return render(req, 'main/user-page.html', context={'visit_acc_images': visit_acc_images,
                                                       'visit_acc_info': visit_acc_info,
                                                       'acc_images': acc_images,
                                                       'acc_info': acc_info,
                                                       'isFollowed': 'active' if isFollowed else '',
                                                       'followers': len(list_of_followers),
                                                       'followings': len(list_of_followings)})


@csrf_exempt
def api_view(req):
    users = User.objects.all()
    data_context = {i.username: i.email for i in users}
    if req.method == 'POST':
        data = json.loads(req.body)
        return JsonResponse(data_context)
    return JsonResponse(data_context)
