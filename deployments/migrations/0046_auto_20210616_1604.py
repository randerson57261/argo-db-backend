# Generated by Django 3.2 on 2021-06-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0045_alter_deployment_deployment_cruise_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='PROFILE_SAMPLING_METHOD_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='PROFILE_SAMPLING_METHOD',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]