# Generated by Django 4.0.3 on 2023-02-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0017_tvshow_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshow',
            name='parts',
        ),
        migrations.AddField(
            model_name='tvshow',
            name='watch_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Part',
        ),
    ]
