# Generated by Django 4.1.4 on 2022-12-23 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_film_video_alter_rating_film_alter_rating_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
