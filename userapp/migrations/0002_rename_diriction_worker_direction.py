# Generated by Django 4.2.1 on 2023-05-22 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='diriction',
            new_name='direction',
        ),
    ]