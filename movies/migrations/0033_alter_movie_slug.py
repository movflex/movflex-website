# Generated by Django 4.0.3 on 2023-09-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0032_auto_20230903_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
