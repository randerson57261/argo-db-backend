# Generated by Django 3.2 on 2021-04-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0003_alter_deployment_platform_maker'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='deployment',
            name='deployments_deployment_CHECKS',
        ),
        migrations.AddConstraint(
            model_name='deployment',
            constraint=models.CheckConstraint(check=models.Q(('TRANS_SYSTEM__in', ['IRIDIUM', 'ARGOS', 'ORBCOMM']), ('START_DATE_QC__in', ['estimated', 'as recorded']), ('LAUNCH_DATE_QC__in', ['estimated', 'as recorded']), ('LAUNCH_POSITION_QC__in', ['estimated', 'as recorded']), ('DEPLOYMENT_TYPE__in', ['RV', 'VOS', 'RRS']), ('WMO_INST_TYPE__in', ['841']), ('PLATFORM_MAKER__in', ['841']), ('LAUNCH_LATITUDE__lte', 90), ('LAUNCH_LATITUDE__gte', -90), ('LAUNCH_LONGITUDE__lte', 180), ('LAUNCH_LONGITUDE__gte', -180)), name='deployments_deployment_CHECKS'),
        ),
    ]
