# Generated by Django 3.2.7 on 2022-01-13 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_teacher_app_join_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='userDetail',
        ),
    ]