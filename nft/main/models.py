from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now



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
    date_of_reg = models.DateTimeField(default=now, blank=True)
    def __str__(self):
        return str(self.customer_name)


class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow')
    owner_of_acc = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')


    def __str__(self):
        return f'{str(self.follower)} - {self.owner_of_acc}'


class Product(models.Model):
    prod_image = models.ImageField(upload_to='./photos/products')
    item_name = models.CharField(max_length=100)
    count_of_prod = models.CharField(max_length=20)
    collect_relat = models.ForeignKey('Collection', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blockchainW = models.ForeignKey('BlockChain', on_delete=models.CASCADE)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    date_of_creat = models.DateTimeField(default=now, blank=True)


    def __str__(self):
        p = Product.objects.get(id=self.id)
        return f'{self.item_name} - {self.author} | {p.item_name} - {p.author}'



class Collection(models.Model):
    name_of_collection = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_collection


class BlockChain(models.Model):
    blockchain_curr = models.CharField(max_length=100)

    def __str__(self):
        return self.blockchain_curr