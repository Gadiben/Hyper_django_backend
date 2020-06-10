from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from backend.forms import ConnexionForm
from django.forms import ValidationError
from django.db import IntegrityError

class UserManagerAsync(UserManager):

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """

        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        # user.save(using=self._db)
        return user

class UserAsync(User):
    objects = UserManagerAsync()

def signup(data):
    form = ConnexionForm(data)
    if form.is_valid():
        username = form.cleaned_data["pseudo"]
        password = form.cleaned_data["password"]
        try:
            user = UserAsync.objects.create_user(username, password=password)
            return user
        except IntegrityError:
            raise ValidationError("The username already exists")
    else:
        raise ValidationError("Error while validating credentials")