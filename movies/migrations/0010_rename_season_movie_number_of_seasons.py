# Generated by Django 4.0.3 on 2023-02-12 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_movie_parts_movie_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='season',
            new_name='number_Of_seasons',
        ),
    ]
