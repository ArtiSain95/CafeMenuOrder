# Generated by Django 2.1.7 on 2019-04-03 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190403_1752'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLogin',
        ),
    ]
