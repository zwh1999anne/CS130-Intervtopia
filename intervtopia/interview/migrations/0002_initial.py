# Generated by Django 4.0.2 on 2022-11-03 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interview', '0001_initial'),
        ('evaluation', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interviewee',
            name='evalForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evalform'),
        ),
        migrations.AddField(
            model_name='interviewee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interview',
            name='problems',
            field=models.ManyToManyField(to='interview.Problem'),
        ),
        migrations.AddField(
            model_name='interview',
            name='viewEE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.interviewee'),
        ),
        migrations.AddField(
            model_name='interview',
            name='viewER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.interviewer'),
        ),
    ]