# Generated by Django 4.0.3 on 2023-02-12 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release_year',
            options={'ordering': ['-year']},
        ),
    ]
