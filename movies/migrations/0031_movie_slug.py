# Generated by Django 4.0.3 on 2023-09-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0030_movie_coming_soon'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
