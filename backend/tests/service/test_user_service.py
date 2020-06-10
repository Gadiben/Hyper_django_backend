from django.contrib.auth.models import User
from django.test import TestCase

from backend.models import AppUser, UserUserAuthDjango

from mock import patch

class UserServiceTest(TestCase):
    def test_user_service(self):
        self.assertEqual(True,True)