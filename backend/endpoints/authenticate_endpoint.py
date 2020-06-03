from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.exceptions import ValidationError 
from backend.forms import ConnexionForm
from django.db.utils import IntegrityError


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
            # return Response({"message":"Test creating user"})
        except IntegrityError:
            raise ValidationError("The username already exists")
    else:
        raise ValidationError("Error while validation credentials")

# class Signup(APIView):
#     def post(self,request):
#         user = signup(request.data)
#         return Response({"message":"Test creating user"})
        # form = ConnexionForm(request.data)
        # if form.is_valid():
        #     username = form.cleaned_data["username"]
        #     password = form.cleaned_data["password"]
        #     try:
        #         user = User.objects.create_user(username, password=password)
        #         return Response({"message":"Test creating user"})
        #     except IntegrityError:
        #         raise ValidationError("The username already exists")
        # else:
        #     raise ValidationError("Error while validation credentials")


class Login(APIView):
    def post(self,request):
        form = ConnexionForm(request.data)
        if form.is_valid():
            username = form.cleaned_data["pseudo"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({"message":"You are logged in"})
            else:
                raise ValidationError("Wrong credentials")
        else:
            raise ValidationError("Error while validation credentials")


class Logout(APIView):
    @method_decorator(login_required(login_url="/hyper/backend"))
    def get(self, request):
        print(request.user)
        print(request.user.is_authenticated)
        logout(request)
        return Response({"message":"You are logged out!"})
