# Generated by Django 2.1.7 on 2019-04-03 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_userlogin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLogin',
        ),
        migrations.DeleteModel(
            name='UserSignUp',
        ),
    ]
