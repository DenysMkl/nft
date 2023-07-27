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