# Generated by Django 3.2 on 2021-05-25 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0012_battery_manufacturers_battery_types_instrument_types_aoml_origin_countries_wmo_recorder_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='deployment_platforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VALUE', models.CharField(max_length=100, unique=True)),
                ('DISPLAY', models.CharField(max_length=200)),
                ('ACTIVE', models.BooleanField()),
                ('SOURCE', models.CharField(max_length=50)),
                ('DESCRIPTION', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Deployment Platforms',
            },
        ),
    ]
