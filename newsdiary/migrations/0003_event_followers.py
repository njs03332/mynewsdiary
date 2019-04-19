# Generated by Django 2.2 on 2019-04-19 07:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsdiary', '0002_auto_20190419_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
