# Generated by Django 3.0.8 on 2020-08-16 12:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_auto_20200811_2127'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together={('user', 'title')},
        ),
    ]