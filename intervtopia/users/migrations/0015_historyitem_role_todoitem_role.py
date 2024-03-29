# Generated by Django 4.0.2 on 2022-11-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_historyitem_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyitem',
            name='role',
            field=models.CharField(choices=[('ER', 'Interviewer'), ('EE', 'Interviewee')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='role',
            field=models.CharField(choices=[('ER', 'Interviewer'), ('EE', 'Interviewee')], max_length=2, null=True),
        ),
    ]
