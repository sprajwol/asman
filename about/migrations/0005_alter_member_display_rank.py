# Generated by Django 3.2.4 on 2021-12-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_member_display_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='display_rank',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]