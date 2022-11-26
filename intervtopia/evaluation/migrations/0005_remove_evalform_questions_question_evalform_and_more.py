# Generated by Django 4.0.2 on 2022-11-23 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_remove_evalform_comments_remove_evalform_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evalform',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='evalform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='evaluation.evalform'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='evaluation.question'),
        ),
        migrations.AlterField(
            model_name='response',
            name='evalform',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response', to='evaluation.evalform'),
        ),
    ]