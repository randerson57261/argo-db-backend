# Generated by Django 3.2 on 2021-05-27 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0036_rename_platform_type_internal_deployment_platform_type'),
        ('choices', '0019_auto_20210526_2004'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='platform_types_internal',
            new_name='platform_types',
        ),
        migrations.AlterModelOptions(
            name='platform_types',
            options={'verbose_name_plural': 'Platform Types'},
        ),
    ]
