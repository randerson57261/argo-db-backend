# Generated by Django 3.2 on 2021-12-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0026_deployment_platforms_c17'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment_platforms_c17',
            name='DESCRIPTION',
            field=models.JSONField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='deployment_platforms_c17',
            name='TYPE',
            field=models.CharField(blank=True, choices=[('R/V', 'R/V'), ('VOS', 'VOS'), ('M/V', 'M/V'), ('AIR', 'AIR')], max_length=25, null=True),
        ),
    ]
