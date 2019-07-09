# Generated by Django 2.2.3 on 2019-07-08 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField()),
                ('GPSx', models.DecimalField(decimal_places=6, max_digits=8)),
                ('GPSy', models.DecimalField(decimal_places=6, max_digits=8)),
                ('AccX', models.DecimalField(decimal_places=5, max_digits=8)),
                ('AccY', models.DecimalField(decimal_places=5, max_digits=8)),
                ('AccZ', models.DecimalField(decimal_places=5, max_digits=8)),
                ('GiroXY', models.DecimalField(decimal_places=4, max_digits=6)),
                ('GiroXZ', models.DecimalField(decimal_places=4, max_digits=6)),
                ('GiroYZ', models.DecimalField(decimal_places=4, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]