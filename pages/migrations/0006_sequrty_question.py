# Generated by Django 4.0.3 on 2023-05-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_delete_sequrty_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequrty_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('name_ar', models.TextField()),
            ],
        ),
    ]
