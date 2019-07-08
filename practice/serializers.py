from rest_framework import serializers
from practice.models import GeoData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = '__all__'