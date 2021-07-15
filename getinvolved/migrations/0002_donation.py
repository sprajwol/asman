# Generated by Django 3.2.4 on 2021-07-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getinvolved', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Applicant Full Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mobile Number')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('project', models.CharField(max_length=100, verbose_name='Project')),
                ('message', models.TextField()),
            ],
        ),
    ]