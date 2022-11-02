# Generated by Django 3.2.16 on 2022-11-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_auto_20221101_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewEE_EvaluationFormDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_text', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewER_EvaluationFormDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_text', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
