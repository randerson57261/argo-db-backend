# Generated by Django 3.2 on 2021-12-14 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0025_tracking_error_types'),
        ('logs', '0010_auto_20210813_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment_tracking',
            name='ERROR_TYPE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='choices.tracking_error_types'),
        ),
    ]
