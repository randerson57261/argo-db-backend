# Generated by Django 3.2 on 2021-06-02 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0007_alter_deployment_tracking_deployment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deployment_tracking',
            options={'ordering': ['DATE'], 'verbose_name_plural': 'Deployment Tracking'},
        ),
    ]