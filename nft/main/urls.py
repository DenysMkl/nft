from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('create', views.createNFT, name='nftcr'),
    path('profile', views.profile, name='prof'),
    path('settings', views.settings, name='sett'),
    path('goods', views.prod_page, name='goods'),
    path('auth', views.Auth.as_view(), name='auth'),
    path('register', views.Register.as_view(), name='reg'),
    path('logout_user', views.logout_user, name='logout'),
    path('<value>', views.profiles)
]