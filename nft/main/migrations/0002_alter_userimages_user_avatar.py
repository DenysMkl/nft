# Generated by Django 4.1.7 on 2023-07-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimages',
            name='user_avatar',
            field=models.ImageField(default='photos/avatars_imgs/user.png', upload_to='photos/avatars_imgs'),
        ),
    ]
