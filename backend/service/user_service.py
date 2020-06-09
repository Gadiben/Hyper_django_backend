from rest_framework import serializers
from backend.service.auth_user_service import signup
from backend.models import AppUser, UserUserAuthDjango

class UserPostSerializer(serializers.Serializer):
    pseudo = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=20)
    password = serializers.CharField()
    date_of_birth = serializers.DateField()
    longitude = serializers.DecimalField(max_digits=4,decimal_places=2)
    latitude = serializers.DecimalField(max_digits=4,decimal_places=2)


class UserService:

    def create(**user_data):
        #Validate credentials 

        #Validate input forum
        input_serializer = UserPostSerializer(data=user_data)
        input_serializer.is_valid(raise_exception=True)
        
        #Validate credentials 
        auth_user = signup(input_serializer.validated_data)
        del input_serializer.validated_data["password"]
        
        #Creat application user
        users = AppUser.objects.all()
        new_id=1 if len(users)==0 else max([el.id for el in users])+1
        instance = AppUser.objects.create(id=new_id,**input_serializer.validated_data)
        instance.save()

        #Commit credentials
        auth_user.save()

        #Save link logic - managing
        userUserAuthDjango = UserUserAuthDjango.objects.create(user_id=instance,auth_id=auth_user)
        userUserAuthDjango.save()
        return userUserAuthDjango