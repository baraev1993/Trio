# Generated by Django 4.1.4 on 2022-12-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('body', models.TextField()),
                ('craeted_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('film', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(null=True, upload_to='films'),
        ),
    ]