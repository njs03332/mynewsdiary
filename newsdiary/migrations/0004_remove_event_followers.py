# Generated by Django 2.2 on 2019-04-19 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsdiary', '0003_event_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='followers',
        ),
    ]
