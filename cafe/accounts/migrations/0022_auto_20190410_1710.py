# Generated by Django 2.1.7 on 2019-04-10 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20190409_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='Price',
            new_name='Item_Price',
        ),
    ]
