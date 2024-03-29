# Generated by Django 3.2 on 2021-04-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0005_transmission_systems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument_types',
            name='VALUE',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='platform_makers',
            name='VALUE',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='platform_types',
            name='VALUE',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sensor_makers',
            name='VALUE',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sensor_models',
            name='VALUE',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sensor_types',
            name='VALUE',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transmission_systems',
            name='VALUE',
            field=models.CharField(max_length=100),
        ),
    ]
