# Generated by Django 3.2 on 2021-04-23 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0019_auto_20210423_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deployment',
            name='PLATFORM_MAKER',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='PLATFORM_TYPE',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='TRANS_SYSTEM',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='WMO_INST_TYPE',
        ),
    ]
