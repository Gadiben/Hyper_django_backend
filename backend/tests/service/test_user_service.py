from django.contrib.auth.models import User
from django.test import TestCase
from django.forms import ValidationError
from backend.models import AppUser, UserUserAuthDjango
from backend.service.user_service import create
from django.db import IntegrityError
from mock import patch, Mock, PropertyMock
from django.forms import ValidationError
from django.db import IntegrityError

@patch('backend.service.user_service.UserPostSerializer',autospec=True)
@patch('backend.service.user_service.signup',autospec=True)
@patch('backend.service.user_service.AppUser.objects',autospec=True)
@patch('backend.service.user_service.UserUserAuthDjango.objects',autospec=True)
class UserServiceTest(TestCase):

    def setUp(self):
        self.user_data = dict(pseudo="user",gender="male",longitude=0,latitude=0,date_of_birth="2001-01-01")
        self.user_1 = AppUser.objects.create(**self.user_data,id=0)
        self.user_data["password"]="123546"

    
    def test_user_service_not_valid(self, m_user_auth, m_app_user, m_signup, m_user_serializer):
        m_user_serializer.return_value = m_user_serializer
        m_user_serializer.is_valid.side_effect = ValidationError("")

        with self.assertRaises(ValidationError):
            user = create(**self.user_data)

    def test_user_service_unable_create_appuser(self, m_user_auth, m_app_user, m_signup, m_user_serializer):
        m_user_serializer.return_value = m_user_serializer
        m_user_serializer.is_valid.return_value = True
        m_app_user.all = PropertyMock(return_value= [self.user_1])
        m_app_user.create = PropertyMock(side_effect=IntegrityError())

        with self.assertRaises(IntegrityError):
            user = create(**self.user_data)

    def test_user_service_unable_create_user_user(self, m_user_auth, m_app_user, m_signup, m_user_serializer):
        m_user_serializer.return_value = m_user_serializer
        m_user_serializer.is_valid.return_value = True
        m_app_user.all = PropertyMock(return_value=[self.user_1])
        m_app_user.create = PropertyMock(return_value=m_app_user)
        m_user_auth.create = PropertyMock(side_effect=IntegrityError())

        m_signup.save = PropertyMock(return_value=m_signup)
        m_app_user.save = PropertyMock(return_value=m_app_user)

        with self.assertRaises(IntegrityError):
            user = create(**self.user_data)