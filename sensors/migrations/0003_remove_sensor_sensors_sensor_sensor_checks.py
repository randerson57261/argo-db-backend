# Generated by Django 3.2 on 2021-04-19 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_auto_20210419_1301'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='sensor',
            name='sensors_sensor_SENSOR_CHECKS',
        ),
    ]
