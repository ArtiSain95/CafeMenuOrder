# Generated by Django 2.1.7 on 2019-04-09 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20190409_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedmeal',
            name='menu',
        ),
        migrations.AddField(
            model_name='orderedmeal',
            name='menu',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_meals', to='accounts.Menu'),
            preserve_default=False,
        ),
    ]
