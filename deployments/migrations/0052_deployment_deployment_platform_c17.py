# Generated by Django 3.2 on 2021-12-14 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0026_deployment_platforms_c17'),
        ('deployments', '0051_alter_deployment_dry_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='DEPLOYMENT_PLATFORM_C17',
            field=models.ForeignKey(blank=True, limit_choices_to={'ACTIVE': True}, null=True, on_delete=django.db.models.deletion.PROTECT, to='choices.deployment_platforms_c17'),
        ),
    ]
