# Generated by Django 3.2 on 2021-04-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0012_auto_20210421_1642'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='sensor',
            name='sensors_sensor_SENSOR_CHECKS',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='SENSOR_MODEL',
            field=models.CharField(blank=True, choices=[('DRUCK_2900PSIA', 'Druck pressure sensor with 2900 PSIA rating'), ('SBE41CP_V3.0c', 'Sea-Bird Scientific SBE 41CP CTD V3.0c'), ('SBE63_V3.2.2', 'SBE63_V3.2.2'), ('SUNA_V2', 'SUNA_V2'), ('SBE41CP_V5.3.4', 'SBE41CP_V5.3.4'), ('MCOMS_FLBBCD', 'MCOMS_FLBBCD'), ('SEAFET', 'SEAFET'), ('MCOMS', 'MCOMS')], max_length=25, null=True),
        ),
        migrations.AddConstraint(
            model_name='sensor',
            constraint=models.CheckConstraint(check=models.Q(('SENSOR__in', ['FLUOROMETER_CHLA', 'TRANSISTOR_PH', 'CTD_CNDC', 'CTD_PRES', 'CTD_TEMP', 'OPTODE_DOXY', 'SPECTROPHOTOMETER_NITRATE', 'FLUOROMETER_CDOM', 'RADIOMETER_PAR', 'BACKSCATTERINGMETER_BBP700', 'PUMP_VOLTAGE', 'CPU_VOLTAGE']), ('SENSOR_MAKER__in', ['JAC', 'SBE', 'MBARI', 'DRUCK', 'SATLANTIC', 'WETLABS']), ('SENSOR_MODEL__in', ['DRUCK_2900PSIA', 'SBE41CP_V3.0c', 'SBE63_V3.2.2', 'SUNA_V2', 'SBE41CP_V5.3.4', 'MCOMS_FLBBCD', 'SEAFET', 'MCOMS'])), name='sensors_sensor_SENSOR_CHECKS'),
        ),
    ]
