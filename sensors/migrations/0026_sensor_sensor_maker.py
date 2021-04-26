# Generated by Django 3.2 on 2021-04-23 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0008_auto_20210423_1043'),
        ('sensors', '0025_alter_sensor_sensor_maker'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='SENSOR_MAKER',
            field=models.ForeignKey(blank=True, limit_choices_to={'ACTIVE': True}, max_length=25, null=True, on_delete=django.db.models.deletion.PROTECT, to='choices.sensor_makers', to_field='VALUE'),
        ),
    ]
