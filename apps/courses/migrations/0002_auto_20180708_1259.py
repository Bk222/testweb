# Generated by Django 2.0.1 on 2018-07-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher_tell',
        ),
        migrations.RemoveField(
            model_name='course',
            name='you_need_know',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_desc',
            field=models.CharField(default='1', max_length=100, verbose_name='教师信息'),
        ),
    ]
