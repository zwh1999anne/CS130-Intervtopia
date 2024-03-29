# Generated by Django 4.0.2 on 2022-11-03 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_value', models.IntegerField(default=0)),
                ('choice_text', models.CharField(max_length=200)),
                ('selected', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('target', models.CharField(choices=[('ER', 'Interviewer'), ('EE', 'Interviewee')], default=0, max_length=2)),
                ('question_ranking', models.IntegerField(default=0)),
                ('question_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('problem_solving', models.IntegerField(default=0)),
                ('communication', models.IntegerField(default=0)),
                ('coding_skill', models.IntegerField(default=0)),
                ('helpful', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EvalForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('rating', models.IntegerField(default=0)),
                ('comments', models.TextField()),
                ('target_role', models.CharField(choices=[('ER', 'Interviewer'), ('EE', 'Interviewee')], max_length=2)),
                ('questions', models.ManyToManyField(to='evaluation.Question')),
                ('response', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='evaluation.response')),
            ],
        ),
    ]
