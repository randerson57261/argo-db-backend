# Generated by Django 3.2 on 2021-04-23 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0006_auto_20210419_1550'),
        ('sensors', '0018_alter_sensor_sensor_maker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='SENSOR',
        ),
    ]
