# Generated by Django 5.1 on 2024-08-09 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0005_photo_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
