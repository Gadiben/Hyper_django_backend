from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from backend.endpoints.user_endpoint import UserViewSet
from backend.service.user_service import UserService
from backend.models import AppUser
from django.contrib.auth import get_user_model

class UserEndpointTests(TestCase):

    
    def setUp(self):
        username="test_user"
        password = "123456"
        user_info_1 = dict(pseudo=username+"1",password=password,gender='male',date_of_birth='2001-01-01',longitude=0,latitude=0)
        user_info_2 = dict(pseudo=username+"2",password=password,gender='male',date_of_birth='2001-01-01',longitude=0,latitude=0)
        self.user_1 = UserService.create(**user_info_1)
        self.user_2 = UserService.create(**user_info_2)


    def test_view_own_profile(self):
        """
        Check if not logged in user 
        """
        
        factory = APIRequestFactory()
        request = factory.get("")
        
        view = UserViewSet.as_view({'get': 'retrieve'})

        # Make an authenticated request to the view...
        force_authenticate(request, user=self.user_1.auth_id)
        response = view(request,pk=self.user_1.auth_id.id)
        # print("response",response.data)
        
        self.assertEqual(response.status_code, 200)
    
    def test_view_different_profile(self):
        """
        Check if not logged in user 
        """
        
        factory = APIRequestFactory()
        request = factory.get("")
        
        view = UserViewSet.as_view({'get': 'retrieve'})

        # Make an authenticated request to the view...
        force_authenticate(request, user=self.user_2.auth_id)
        response = view(request,pk=self.user_1.auth_id.id)
        # print("response",response.data)
        
        self.assertEqual(response.status_code, 403)