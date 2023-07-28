from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.db import models

class Customer_images(models.Model):
    customer_bg = models.ImageField(upload_to='./photos/backgr_imgs', null=True, blank=True)
    customer_avatar = models.ImageField(upload_to='./photos/avatars_imgs', null=True, blank=True)
    customer_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.customer_name)


class Customer_data(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    user_name = models.CharField(max_length=30, null=True, blank=True)
    inst_link = models.CharField(max_length=100, null=True, blank=True)
    tg_link = models.CharField(max_length=100, null=True, blank=True)
    descr = models.CharField(max_length=100, null=True, blank=True)
    customer_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.customer_name)