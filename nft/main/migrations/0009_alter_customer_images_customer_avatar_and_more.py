# Generated by Django 4.1.7 on 2023-07-27 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_alter_customer_images_customer_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_images',
            name='customer_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='./photos/avatars_imgs'),
        ),
        migrations.AlterField(
            model_name='customer_images',
            name='customer_bg',
            field=models.ImageField(blank=True, null=True, upload_to='./photos/backgr_imgs'),
        ),
        migrations.AlterField(
            model_name='customer_images',
            name='customer_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
