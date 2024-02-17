# Generated by Django 4.0.3 on 2023-02-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0011_alter_tvshow_parts_alter_tvshow_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='parts',
            field=models.ManyToManyField(blank=True, null=True, to='tvshows.part'),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tvshows.tag'),
        ),
    ]
