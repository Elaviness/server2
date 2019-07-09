# Generated by Django 2.2.3 on 2019-07-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geodata',
            name='add_date',
        ),
        migrations.AddField(
            model_name='geodata',
            name='GPSstring',
            field=models.CharField(default=0, max_length=70),
        ),
        migrations.AddField(
            model_name='geodata',
            name='GPStime',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='geodata',
            name='GPSx',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='GPSy',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]