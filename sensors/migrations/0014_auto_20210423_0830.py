# Generated by Django 3.2 on 2021-04-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0013_auto_20210421_1648'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='sensor',
            name='sensors_sensor_SENSOR_CHECKS',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='SENSOR',
            field=models.CharField(choices=[('FLUOROMETER_CHLA', 'FLUOROMETER_CHLA'), ('TRANSISTOR_PH', 'TRANSISTOR_PH'), ('CTD_CNDC', 'CTD_CNDC'), ('CTD_PRES', 'CTD_PRES'), ('CTD_TEMP', 'CTD_TEMP'), ('OPTODE_DOXY', 'OPTODE_DOXY'), ('SPECTROPHOTOMETER_NITRATE', 'SPECTROPHOTOMETER_NITRATE'), ('FLUOROMETER_CDOM', 'FLUOROMETER_CDOM'), ('RADIOMETER_PAR', 'RADIOMETER_PAR'), ('BACKSCATTERINGMETER_BBP700', 'BACKSCATTERINGMETER_BBP700'), ('PUMP_VOLTAGE', 'PUMP_VOLTAGE'), ('CPU_VOLTAGE', 'CPU_VOLTAGE')], max_length=50),
        ),
    ]