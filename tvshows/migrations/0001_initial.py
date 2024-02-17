# Generated by Django 4.0.3 on 2023-01-31 15:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channels', '0001_initial'),
        ('cast_and_crew', '0002_release_year_director_job_writer_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nam', models.CharField(max_length=80)),
                ('tvshow_name', models.CharField(max_length=80)),
                ('comment', models.TextField()),
                ('evalute', models.DecimalField(decimal_places=1, max_digits=2)),
                ('comment_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tvshow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('season', models.IntegerField()),
                ('poster', models.ImageField(upload_to='photos/posters')),
                ('video_url', models.TextField()),
                ('download_url', models.TextField()),
                ('description', models.TextField()),
                ('description_ar', models.TextField(default='none')),
                ('imbd', models.DecimalField(decimal_places=1, max_digits=2)),
                ('number_votes', models.IntegerField()),
                ('gross', models.IntegerField()),
                ('typee', models.TextField(default='Tvshows', editable=False)),
                ('is_trend', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now)),
                ('casts', models.ManyToManyField(to='cast_and_crew.cast')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cast_and_crew.category')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='channels.channel')),
                ('director', models.ManyToManyField(to='cast_and_crew.director')),
                ('release_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cast_and_crew.release_year')),
                ('writer', models.ManyToManyField(to='cast_and_crew.writer')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
