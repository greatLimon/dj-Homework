# Generated by Django 5.1.4 on 2024-12-07 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_temperaturemeasurment_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperaturemeasurment',
            name='sensor_id',
        ),
    ]
