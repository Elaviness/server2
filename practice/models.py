from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class GeoData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    GPSstring = models.CharField(max_length=70, default='', null=True)

    GPStime = models.BigIntegerField(default=0, null=True)
    GPSx = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)
    GPSy = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)

    AccX = models.DecimalField(max_digits=10, decimal_places=5, default=0, null=True)
    AccY = models.DecimalField(max_digits=10, decimal_places=5, default=0, null=True)
    AccZ = models.DecimalField(max_digits=10, decimal_places=5, default=0, null=True)

    GiroXY = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)
    GiroXZ = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)
    GiroYZ = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)

class ForCallculations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    GPSstring = models.CharField(max_length=70, default='', null=True)

    GPStime = models.BigIntegerField(default=0, null=True)
    GPSx = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)
    GPSy = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)

    AccX = models.DecimalField(max_digits=10, decimal_places=5, default=0, null=True)
    AccY = models.DecimalField(max_digits=10, decimal_places=5, default=0, null=True)
    AccZ = models.DecimalField(max_digits=10, decimal_places=5, default=0, null=True)

    GiroXY = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)
    GiroXZ = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)
    GiroYZ = models.DecimalField(max_digits=8, decimal_places=4, default=0, null=True)

    Speed = models.DecimalField(max_digits=8, decimal_places=5, default=0, null=True)
    AngAcc = models.DecimalField(max_digits=6, decimal_places=4, default=0, null=True)
    NumOvertake = models.BigIntegerField()
    SpeedType_Choices = (
        ('Lx', 'Низкая скорость'),
        ('NR', 'Средняя скорость'),
        ('Hg', 'Высокая скорость'),
    )
    SpeedType = models.CharField(max_length=2,
                                 choices=SpeedType_Choices,
                                 default='NR')
    UserType_Choices = (
        ('CM', 'Спокойное вождение'),
        ('CF', 'Уверенный водитель'),
        ('DR', 'Опасное вождение'),
    )
    UserType = models.CharField(max_length=2,
                                 choices=UserType_Choices,
                                 default='CM')

