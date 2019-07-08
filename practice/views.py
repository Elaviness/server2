from rest_framework import generics
from practice.serializers import DataSerializer

# Create your views here.
class DataCreate(generics.CreateAPIView):
    serializer_class = DataSerializer

