# Generated by Django 5.1 on 2024-08-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0004_photo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
