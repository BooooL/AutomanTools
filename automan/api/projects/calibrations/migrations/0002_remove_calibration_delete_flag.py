# Generated by Django 2.2.2 on 2020-01-22 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calibrations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calibration',
            name='delete_flag',
        ),
    ]
