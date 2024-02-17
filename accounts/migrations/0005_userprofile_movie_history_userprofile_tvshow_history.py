# Generated by Django 4.0.3 on 2023-05-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0020_alter_tvshow_options_and_more'),
        ('movies', '0025_alter_movie_options_and_more'),
        ('accounts', '0004_remove_userprofile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='movie_history',
            field=models.ManyToManyField(related_name='movie_history', to='movies.movie'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tvshow_history',
            field=models.ManyToManyField(related_name='tvshow_history', to='tvshows.tvshow'),
        ),
    ]