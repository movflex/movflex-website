# Generated by Django 4.0.3 on 2023-01-11 17:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cast_and_crew', '0001_initial'),
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nam', models.CharField(max_length=80)),
                ('movie_name', models.CharField(max_length=80)),
                ('comment', models.TextField()),
                ('evalute', models.DecimalField(decimal_places=1, max_digits=2)),
                ('comment_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('season', models.IntegerField()),
                ('poster', models.ImageField(upload_to='photos/posters')),
                ('video_url', models.TextField()),
                ('description', models.TextField()),
                ('description_ar', models.TextField(default='none')),
                ('imbd', models.DecimalField(decimal_places=1, max_digits=2)),
                ('number_votes', models.IntegerField()),
                ('gross', models.IntegerField()),
                ('released_date', models.DateField(default=datetime.datetime.now)),
                ('is_trend', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now)),
                ('casts', models.ManyToManyField(to='cast_and_crew.cast')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cast_and_crew.category')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='channels.channel')),
                ('director', models.ManyToManyField(to='cast_and_crew.director')),
                ('writer', models.ManyToManyField(to='cast_and_crew.writer')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
