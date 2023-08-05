# Generated by Django 4.1.7 on 2023-08-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_follower_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='follower',
            constraint=models.UniqueConstraint(fields=('follower', 'owner_of_acc'), name='follow system'),
        ),
    ]