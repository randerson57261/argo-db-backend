# Generated by Django 3.2 on 2021-04-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('env_data', '0013_cycle_metadata_phcountervolts'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycle_metadata',
            name='pHCounterAmps',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
