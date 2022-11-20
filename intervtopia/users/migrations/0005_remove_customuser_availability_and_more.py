# Generated by Django 4.0.2 on 2022-11-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_availability_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='availability',
        ),
        migrations.AddField(
            model_name='customuser',
            name='availability',
            field=models.ManyToManyField(to='users.Availability'),
        ),
    ]
