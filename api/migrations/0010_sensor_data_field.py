# Generated by Django 2.1.5 on 2019-08-27 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_trafficreading'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='data_field',
            field=models.CharField(default='', max_length=100),
        ),
    ]
