# Generated by Django 3.2 on 2021-12-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0050_deployment_dry_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='DRY_WEIGHT',
            field=models.FloatField(blank=True, null=True, verbose_name='DRY WEIGHT (g)'),
        ),
    ]
