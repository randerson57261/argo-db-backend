# Generated by Django 3.2 on 2021-12-16 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0030_delete_deployment_platforms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deployment_platforms_c17',
            options={'ordering': ['-ACTIVE', 'VALUE'], 'verbose_name_plural': 'Deployment Platforms C17'},
        ),
    ]
