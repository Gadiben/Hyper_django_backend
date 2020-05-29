from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
class UserGetSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=0)


class UserGetOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pseudo', 'gender','date_of_birth')


class UserEndpoint(APIView):

    def get(self, request, *args, **kwargs):
        input_serializer = UserGetSerializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)

        instance = get_object_or_404(User, pk=input_serializer.data['id'])
        output_serializer = UserGetOutputSerializer(instance)
        return Response(output_serializer.data)

    def post(self, request, *args, **kwargs):
        input_serializer = UserGetSerializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)

        instance = get_object_or_404(User, pk=input_serializer.data['id'])
        output_serializer = UserGetOutputSerializer(instance)
        return Response()

