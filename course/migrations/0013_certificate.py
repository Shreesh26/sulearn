# Generated by Django 3.2.7 on 2022-01-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20220115_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
    ]
