# Generated by Django 2.1.7 on 2019-04-11 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20190410_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_item_price', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Menu')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderedmeal',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='orderedmeal',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderedmeal',
            name='meal_items',
            field=models.ManyToManyField(related_name='ordered_item', to='accounts.MealItem'),
        ),
    ]
