# Generated by Django 3.2 on 2021-12-16 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0053_auto_20211216_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deployment',
            name='DEPLOYMENT_PLATFORM',
        ),
    ]
