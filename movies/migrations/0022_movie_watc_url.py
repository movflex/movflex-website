# Generated by Django 4.0.3 on 2023-02-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_remove_movie_parts_delete_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watc_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
