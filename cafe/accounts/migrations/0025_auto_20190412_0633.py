# Generated by Django 2.1.7 on 2019-04-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20190411_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedmeal',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=8, null=True),
        ),
    ]
