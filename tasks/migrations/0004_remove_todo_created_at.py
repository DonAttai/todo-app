# Generated by Django 3.0.8 on 2020-08-11 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
    ]
