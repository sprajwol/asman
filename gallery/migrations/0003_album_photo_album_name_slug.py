# Generated by Django 3.2.4 on 2021-07-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_image_photo_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='photo_album_name_slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
