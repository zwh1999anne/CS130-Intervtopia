# Generated by Django 4.0.2 on 2022-11-29 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friend_and_message', '0005_friendship_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='myText',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='time',
        ),
    ]
