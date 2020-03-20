# Generated by Django 2.1.5 on 2019-02-04 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190201_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airqualityreading',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='air_readings', to='api.Sensor'),
        ),
        migrations.AlterField(
            model_name='motionreading',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motion_readings', to='api.Sensor'),
        ),
        migrations.AlterField(
            model_name='soundreading',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sound_readings', to='api.Sensor'),
        ),
    ]
