# Generated by Django 4.0.3 on 2023-05-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0022_alter_tvshow_watch_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='watch_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
