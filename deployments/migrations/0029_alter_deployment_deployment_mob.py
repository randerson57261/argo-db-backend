# Generated by Django 3.2 on 2021-05-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0028_auto_20210525_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='DEPLOYMENT_MOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]