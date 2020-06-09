from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.exceptions import ValidationError 
from backend.forms import ConnexionForm
from django.db.utils import IntegrityError




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
