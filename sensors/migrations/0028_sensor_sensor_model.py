# Generated by Django 3.2 on 2021-04-23 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0008_auto_20210423_1043'),
        ('sensors', '0027_remove_sensor_sensor_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='SENSOR_MODEL',
            field=models.ForeignKey(blank=True, limit_choices_to={'ACTIVE': True}, max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, to='choices.sensor_models', to_field='VALUE'),
        ),
    ]
