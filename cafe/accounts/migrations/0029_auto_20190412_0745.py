# Generated by Django 2.1.7 on 2019-04-12 07:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20190412_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealitem',
            name='menu',
        ),
        migrations.AddField(
            model_name='mealitem',
            name='menu',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='accounts.Menu'),
            preserve_default=False,
        ),
    ]
