from rest_framework import generics
from practice.serializers import *

# Create your views here.
class DataCreate(generics.CreateAPIView):
    serializer_class = DataSerializer

class DataCalc(generics.CreateAPIView):
    serializer_class = CalcSerializer