# Generated by Django 4.0.2 on 2022-11-20 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Calender',
            new_name='Calendar',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='availability',
            new_name='calendar',
        ),
    ]
