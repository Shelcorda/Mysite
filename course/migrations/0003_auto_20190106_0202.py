# Generated by Django 2.0.1 on 2019-01-05 18:02

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, upload_to=course.models.user_directory_path),
        ),
    ]