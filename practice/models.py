from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class GeoData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GPSstring = models.CharField(max_length=70, default='')

    GPStime = models.BigIntegerField(default=0)
    GPSx = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    GPSy = models.DecimalField(max_digits=8, decimal_places=4, default=0)

    AccX = models.DecimalField(max_digits=10, decimal_places=5)
    AccY = models.DecimalField(max_digits=10, decimal_places=5)
    AccZ = models.DecimalField(max_digits=10, decimal_places=5)

    GiroXY = models.DecimalField(max_digits=8, decimal_places=4)
    GiroXZ = models.DecimalField(max_digits=8, decimal_places=4)
    GiroYZ = models.DecimalField(max_digits=8, decimal_places=4)

class ForCallculations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GPSstring = models.CharField(max_length=70, default='')

    GPStime = models.BigIntegerField(default=0)
    GPSx = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    GPSy = models.DecimalField(max_digits=8, decimal_places=4, default=0)

    AccX = models.DecimalField(max_digits=10, decimal_places=5)
    AccY = models.DecimalField(max_digits=10, decimal_places=5)
    AccZ = models.DecimalField(max_digits=10, decimal_places=5)

    GiroXY = models.DecimalField(max_digits=8, decimal_places=4)
    GiroXZ = models.DecimalField(max_digits=8, decimal_places=4)
    GiroYZ = models.DecimalField(max_digits=8, decimal_places=4)

    Speed = models.DecimalField(max_digits=8, decimal_places=5)
    AngAcc = models.DecimalField(max_digits=6, decimal_places=4)
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

