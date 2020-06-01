from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .user_serializers import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
