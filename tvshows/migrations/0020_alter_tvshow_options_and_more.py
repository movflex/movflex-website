# Generated by Django 4.0.3 on 2023-02-26 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0019_rename_number_of_seasons_tvshow_season'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tvshow',
            options={'ordering': ['release_year']},
        ),
        migrations.RenameField(
            model_name='tvshow',
            old_name='number_votes',
            new_name='number_views',
        ),
    ]