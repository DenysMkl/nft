# Generated by Django 4.1.7 on 2023-07-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_images',
            name='customer_avatar',
            field=models.ImageField(null=True, upload_to='./photos/avatars_imgs'),
        ),
        migrations.AlterField(
            model_name='customer_images',
            name='customer_bg',
            field=models.ImageField(null=True, upload_to='./photos/backgr_imgs'),
        ),
    ]
