# Generated by Django 4.0.3 on 2023-09-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0003_remove_channel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]