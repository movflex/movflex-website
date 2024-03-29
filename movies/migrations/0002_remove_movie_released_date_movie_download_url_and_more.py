# Generated by Django 4.0.3 on 2023-01-31 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast_and_crew', '0002_release_year_director_job_writer_job'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='released_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='download_url',
            field=models.TextField(default=2020),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.ForeignKey(default=2020, on_delete=django.db.models.deletion.PROTECT, to='cast_and_crew.release_year'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='typee',
            field=models.TextField(default='Movies', editable=False),
        ),
    ]
