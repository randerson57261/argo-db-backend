# Generated by Django 3.2 on 2021-05-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('env_data', '0019_auto_20210503_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycle_metadata',
            name='AirBladderPressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle_metadata',
            name='AirPumpAmps',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle_metadata',
            name='AirPumpVolts',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle_metadata',
            name='BuoyancyPumpAmps',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle_metadata',
            name='BuoyancyPumpVolts',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle_metadata',
            name='QuiescentAmps',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle_metadata',
            name='QuiescentVolts',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle_metadata',
            name='Sbe41cpAmps',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cycle_metadata',
            name='Sbe41cpVolts',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
