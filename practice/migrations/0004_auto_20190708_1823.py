# Generated by Django 2.2.3 on 2019-07-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_auto_20190708_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geodata',
            name='GPStime',
            field=models.BigIntegerField(default=0),
        ),
    ]
