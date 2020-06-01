from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from backend.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pseudo', 'gender', 'date_of_birth', 'longitude', 'latitude')

class UserPostSerializer(serializers.Serializer):
    pseudo = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=20)
    date_of_birth = serializers.DateField()
    longitude = serializers.DecimalField(max_digits=4,decimal_places=2)
    latitude = serializers.DecimalField(max_digits=4,decimal_places=2)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        input_serializer = UserPostSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        users = User.objects.all()
        new_id=max([el.id for el in users])+1
        instance = User.objects.get_or_create(id=new_id,**input_serializer.validated_data)
        output_serializer = UserSerializer(instance)
        return Response(input_serializer.data)

