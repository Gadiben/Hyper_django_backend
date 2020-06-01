from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .endpoints.user_endpoint import UserViewSet
from .endpoints.post_endpoint import PostViewSet
from .endpoints.media_endpoint import MediaViewSet, FilmViewSet,TvshowViewSet,VideoGameViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'medias', MediaViewSet)
router.register(r'films', FilmViewSet)
router.register(r'tv_shows', TvshowViewSet)
router.register(r'video_games', VideoGameViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
