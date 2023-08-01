# Generated by Django 3.2.16 on 2023-08-01 11:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='following'),
        ),
        migrations.DeleteModel(
            name='User_1',
        ),
    ]