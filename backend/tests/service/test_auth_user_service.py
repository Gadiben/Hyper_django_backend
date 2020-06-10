from django.contrib.auth.models import User
from django.test import TestCase
from django.forms import ValidationError
from backend.models import AppUser, UserUserAuthDjango
from backend.service.auth_user_service import signup
from django.db import IntegrityError
from mock import patch, Mock

class AuthUserServiceTest(TestCase):

    def setUp(self):
        self.form_data = {"pseudo":"user","password":"123546"}

    @patch('backend.service.auth_user_service.ConnexionForm',autospec=True)
    def test_auth_user_service_invalid_creadentials(self, mock_connexion_form):
        m_connexion_form = mock_connexion_form.return_value
        m_connexion_form.is_valid.return_value = False

        with self.assertRaises(ValidationError):
            user = signup(self.form_data)

    @patch('backend.service.auth_user_service.ConnexionForm',autospec=True)
    @patch('backend.service.auth_user_service.UserAsync.objects.create_user',autospec=True)
    def test_auth_user_service_unable_create_user(self, mock_create_user, mock_connexion_form):
        m_connexion_form = mock_connexion_form.return_value
        m_connexion_form.is_valid.return_value = True
        m_connexion_form.cleaned_data.return_value = self.form_data

        mock_create_user.side_effect = IntegrityError()
        with self.assertRaises(IntegrityError):
            user = signup(self.form_data)
            mock_create_user.assert_called_once()