# Generated by Django 3.2.6 on 2021-08-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0048_rename_purchace_order_deployment_purchase_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='IMEI',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='deployment',
            name='SIM',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
    ]
