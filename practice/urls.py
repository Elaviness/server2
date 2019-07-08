from django.contrib import admin
from django.urls import path,include
from practice.views import *

urlpatterns = [
    path('add_data', DataCreate.as_view()),
]
