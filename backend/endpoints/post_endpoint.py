from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.reverse import reverse


from .media_endpoint import MediaSerializer
from .user_endpoint import UserSerializer

from backend.models import Post
from backend.urls import *
class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # media = MediaSerializer()
    user_url = serializers.SerializerMethodField()
    media_info_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('publish_time', 'text_content', 
        'media_url','user','fanart','media','user_url','media_info_url')

    def get_user_url(self, Post):
        
        return "/users/"+str(Post.user.id)
    def get_media_info_url(self, Post):
        return "/medias/"+str(Post.media.id)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        input_serializer = PostSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        users = Post.objects.all()
        new_id=max([el.id for el in users])+1
        instance = Post.objects.get_or_create(id=new_id,**input_serializer.validated_data)
        output_serializer = PostSerializer(instance)
        return Response(input_serializer.data)
