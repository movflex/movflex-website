# Generated by Django 4.0.3 on 2023-06-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0024_alter_tvshow_watch_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='coming_soon',
            field=models.BooleanField(default=False),
        ),
    ]
