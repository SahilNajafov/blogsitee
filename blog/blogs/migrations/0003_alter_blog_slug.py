# Generated by Django 4.0.4 on 2022-05-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, unique=True),
        ),
    ]
