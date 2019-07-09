from rest_framework import serializers
from practice.models import *

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = '__all__'

class CalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForCallculations
        fields = '__all__'