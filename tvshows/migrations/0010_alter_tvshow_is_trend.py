# Generated by Django 4.0.3 on 2023-02-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0009_rename_season_tvshow_number_of_seasons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='is_trend',
            field=models.BooleanField(default=False),
        ),
    ]
