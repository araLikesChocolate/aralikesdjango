# Generated by Django 2.2 on 2019-04-30 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ML', '0003_auto_20190429_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='url',
            new_name='image_path',
        ),
    ]