# Generated by Django 4.0.3 on 2023-05-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0020_alter_tvshow_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='watch_url',
            field=models.TextField(),
        ),
    ]
