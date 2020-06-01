from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from backend.models import Platforms
from backend.models import FanartType

class FanartTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FanartType
        fields = ('name',)

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platforms
        fields = ('name',)