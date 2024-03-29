# Generated by Django 3.2 on 2021-04-23 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0007_alter_sensor_types_value'),
        ('sensors', '0023_remove_sensor_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='SENSOR',
            field=models.ForeignKey(default='CTD_PRES', limit_choices_to={'ACTIVE': True}, max_length=50, on_delete=django.db.models.deletion.PROTECT, to='choices.sensor_types', to_field='VALUE'),
            preserve_default=False,
        ),
    ]
