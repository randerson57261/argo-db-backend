# Generated by Django 3.2 on 2021-12-16 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0011_deployment_tracking_error_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deployment_tracking',
            options={'ordering': ['-DATE'], 'verbose_name_plural': 'Deployment Tracking'},
        ),
    ]