# Generated by Django 2.2.2 on 2020-01-22 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('originals', '0002_auto_20200115_0430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='original',
            name='delete_flag',
        ),
    ]