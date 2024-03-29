# Generated by Django 4.0.3 on 2023-02-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0005_tag_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='poster',
            field=models.ImageField(default=1, upload_to='photos/posters/tvshows_parts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='poster',
            field=models.ImageField(upload_to='photos/posters/tvshows'),
        ),
    ]
