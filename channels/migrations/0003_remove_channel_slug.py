# Generated by Django 4.0.3 on 2023-02-13 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0002_channel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='slug',
        ),
    ]
