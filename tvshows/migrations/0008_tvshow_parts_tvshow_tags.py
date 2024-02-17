# Generated by Django 4.0.3 on 2023-02-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0007_remove_tvshow_download_url_remove_tvshow_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='parts',
            field=models.ManyToManyField(to='tvshows.part'),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='tags',
            field=models.ManyToManyField(to='tvshows.tag'),
        ),
    ]
