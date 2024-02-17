# Generated by Django 4.0.3 on 2023-01-11 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/profile/%Y/%m/%d')),
                ('country', models.CharField(max_length=80)),
                ('movie_favorits', models.ManyToManyField(related_name='movie_favorits', to='movies.movie')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_history', models.ManyToManyField(related_name='user_history', to='movies.movie')),
            ],
        ),
    ]
