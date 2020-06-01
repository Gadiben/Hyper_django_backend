from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .enums_serializer import PlatformSerializer

from backend.models import Media
from backend.models import Film
from backend.models import Tvshow
from backend.models import VideoGame

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('release_date', 'title', 'description','image')

class FilmSerializer(serializers.ModelSerializer):
    id = MediaSerializer()
    class Meta:
        model = Film
        fields = ('id','duration')

class TvshowSerializer(serializers.ModelSerializer):
    id = MediaSerializer()
    class Meta:
        model = Tvshow
        fields = ('id','season_number')

class VideoGameSerializer(serializers.ModelSerializer):
    id = MediaSerializer()
    platform = PlatformSerializer()
    class Meta:
        model = VideoGame
        fields = ('id','platform')

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all().order_by('id')
    serializer_class = MediaSerializer
    
class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by('id')
    serializer_class = FilmSerializer

class TvshowViewSet(viewsets.ModelViewSet):
    queryset = Tvshow.objects.all().order_by('id')
    serializer_class = TvshowSerializer
    
class VideoGameViewSet(viewsets.ModelViewSet):
    queryset = VideoGame.objects.all().order_by('id')
    serializer_class = VideoGameSerializer