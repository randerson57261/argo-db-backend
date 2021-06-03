# Generated by Django 3.2 on 2021-05-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0016_auto_20210526_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='platform_types_internal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PLATFORM_TYPE', models.CharField(max_length=25, unique=True)),
                ('ACTIVE', models.BooleanField()),
                ('DESCRIPTION', models.CharField(max_length=200)),
                ('R08_WMO', models.CharField(blank=True, max_length=25, null=True)),
                ('R23_ARGO', models.CharField(blank=True, max_length=25, null=True)),
                ('R23_ARGO_KEY', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'verbose_name_plural': 'Platform Types Internal',
            },
        ),
    ]