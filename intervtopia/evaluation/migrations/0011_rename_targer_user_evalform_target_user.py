# Generated by Django 4.0.2 on 2022-12-02 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0010_evalform_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evalform',
            old_name='targer_user',
            new_name='target_user',
        ),
    ]
