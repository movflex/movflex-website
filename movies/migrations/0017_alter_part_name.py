# Generated by Django 4.0.3 on 2023-02-13 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_alter_movie_casts_alter_movie_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movies.movie'),
        ),
    ]
