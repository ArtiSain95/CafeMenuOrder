# Generated by Django 2.1.7 on 2019-04-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_userlogin_usersignup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('Category', models.CharField(choices=[('drinks', 'Drinks'), ('fastfood', 'Fastfood'), ('deserts', 'Deserts')], default='drinks', max_length=100)),
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Item', models.CharField(max_length=200)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
