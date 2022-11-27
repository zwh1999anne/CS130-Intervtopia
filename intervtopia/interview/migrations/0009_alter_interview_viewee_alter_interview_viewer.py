# Generated by Django 4.0.2 on 2022-11-27 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0008_remove_interview_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='viewEE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='interview',
            name='viewER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewer', to=settings.AUTH_USER_MODEL),
        ),
    ]