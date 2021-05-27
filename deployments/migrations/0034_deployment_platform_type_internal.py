# Generated by Django 3.2 on 2021-05-26 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0017_platform_types_internal'),
        ('deployments', '0033_alter_deployment_deployer'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='PLATFORM_TYPE_INTERNAL',
            field=models.ForeignKey(blank=True, limit_choices_to={'ACTIVE': True}, max_length=25, null=True, on_delete=django.db.models.deletion.PROTECT, to='choices.platform_types_internal', to_field='PLATFORM_TYPE'),
        ),
    ]
