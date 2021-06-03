# Generated by Django 3.2 on 2021-05-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0014_auto_20210525_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment_platforms',
            name='TYPE',
            field=models.CharField(choices=[('R/V', 'R/V'), ('VOS', 'VOS'), ('M/V', 'M/V'), ('AIR', 'AIR')], default='R/V', max_length=25),
            preserve_default=False,
        ),
    ]