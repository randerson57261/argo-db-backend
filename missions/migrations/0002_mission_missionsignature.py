# Generated by Django 3.2 on 2021-04-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='MissionSignature',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
