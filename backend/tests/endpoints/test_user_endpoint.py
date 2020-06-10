from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from backend.endpoints.user_endpoint import UserViewSet
from backend.service.user_service import UserService
from backend.models import AppUser,UserUserAuthDjango
from django.contrib.auth import get_user_model

from mock import patch

class AppUserMock:
    objects=[]

class UserEndpointTests(TestCase):
    
    def setUp(self):
        username="test_user"
        password = "123456"
        user_info_1 = dict(pseudo=username+"1",password=password,gender='male',date_of_birth='2001-01-01',longitude=0,latitude=0)
        user_info_2 = dict(pseudo=username+"2",password=password,gender='male',date_of_birth='2001-01-01',longitude=0,latitude=0)
        self.user_info_3 = dict(pseudo=username+"3",password=password,gender='male',date_of_birth='2001-01-01',longitude=0,latitude=0)
        self.user_1 = UserService.create(**user_info_1)
        self.user_2 = UserService.create(**user_info_2)
        
    
    def retrieve_profil_test(self, user, user_profil, response_code):
        factory = APIRequestFactory()
        request = factory.get("")
        view = UserViewSet.as_view({'get': 'retrieve'})
        force_authenticate(request, user=user.auth_id)
        response = view(request, pk=user_profil.auth_id.id)

        self.assertEqual(response.status_code, response_code)

    # @patch('backend.endpoints.user_endpoint.AppUser.objects', AppUserMock.objects)
    # def test_user_creation(self):
    #     factory = APIRequestFactory()
    #     request = factory.post("",self.user_info_3)
    #     view = UserViewSet.as_view({'post': 'create'})
    #     response = view(request)

    #     print(response.data)
    #     self.assertEqual(response.data,self.user_info_3)
    #     # self.assertEqual(response.status_code, response_code)
    #     # self.assertEqual(response.data, self.user_info_1)

    def test_view_own_profile(self):
        """
        Check if not logged in user 
        """
        self.retrieve_profil_test(self.user_1, self.user_1, 200)        
    
    def test_view_different_profile(self):
        """
        Check if not logged in user 
        """
        self.retrieve_profil_test(self.user_2, self.user_1, 403)