# Generated by Django 4.0.3 on 2023-01-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast_and_crew', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='job',
            field=models.TextField(default='Director', editable=False),
        ),
        migrations.AddField(
            model_name='writer',
            name='job',
            field=models.TextField(default='Writer', editable=False),
        ),
    ]