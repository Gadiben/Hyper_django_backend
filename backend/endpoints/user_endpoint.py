from rest_framework.permissions import IsAuthenticated, BasePermission 

from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from backend.forms import ConnexionForm
from backend.models import User, UserUserAuthDjango
from .authenticate_endpoint import signup

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pseudo', 'gender', 'date_of_birth', 'longitude', 'latitude')

class UserPostSerializer(serializers.Serializer):
    pseudo = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=20)
    password = serializers.CharField()
    date_of_birth = serializers.DateField()
    longitude = serializers.DecimalField(max_digits=4,decimal_places=2)
    latitude = serializers.DecimalField(max_digits=4,decimal_places=2)
    
class ViewProfil(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            user_user_auth = UserUserAuthDjango.objects.get(auth_id=request.user)
            return int(user_user_auth.user_id.id)==int(view.kwargs['pk'])

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        #Validate input forum
        input_serializer = UserPostSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        
        #Validate credentials 
        auth_user = signup(input_serializer.validated_data)
        del input_serializer.validated_data["password"]

        #Creat application user
        users = User.objects.all()
        new_id=max([el.id for el in users])+1
        instance,existed = User.objects.get_or_create(id=new_id,**input_serializer.validated_data)
        
        #Commit credentials
        auth_user.save()

        #Save link logic - managing
        userUserAuthDjango = UserUserAuthDjango.objects.create(user_id=instance,auth_id=auth_user).save()

        #Response
        output_serializer = UserSerializer(instance)
        return Response(output_serializer.data)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []
        if self.action == 'retrieve':
            permission_classes += [ViewProfil]
        return [permission() for permission in permission_classes]

