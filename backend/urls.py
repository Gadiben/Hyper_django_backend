from django.contrib import admin
from django.urls import path, include
from .user_serializers import UserEndpoint

urlpatterns = [
    path('user/',UserEndpoint.as_view()),
]
