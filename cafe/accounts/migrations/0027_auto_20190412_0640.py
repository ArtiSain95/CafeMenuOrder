# Generated by Django 2.1.7 on 2019-04-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20190412_0639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedmeal',
            name='meal_items',
        ),
        migrations.AddField(
            model_name='orderedmeal',
            name='meal_items',
            field=models.ManyToManyField(related_name='ordered_item', to='accounts.MealItem'),
        ),
    ]
