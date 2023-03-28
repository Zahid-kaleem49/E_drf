import base64
from abc import ABC
from datetime import datetime

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView, Response
from django.shortcuts import render

from .models import User
from .serializers import UserSerializers
from E_DRF.utils import is_valid
from django.db import connection
from django.contrib.auth.hashers import make_password



# Create your views here.


# class BasicAuthentication(BaseAuthentication, ABC):
#     def authenticate(self, request):
#         auth = request.data.get('authenticators', "").split()
#         if not auth or auth[0].lower() != "basic":
#             return None
#         if len(auth) == 1:
#             raise exceptions.AuthenticationFailed("Invalid basic header. No credentials provided.")
#         if len(auth) > 2:
#             raise exceptions.AuthenticationFailed("Invalid basic header. Credential string is not properly formatted")
#         try:
#             auth_decoded = base64.b64decode(auth[1]).decode("utf-8")
#             username, password = auth_decoded.split(":")
#         except (UnicodeDecodeError, ValueError):
#             raise exceptions.AuthenticationFailed("Invalid basic header. Credentials not correctly encoded")
#
#         return self.authenticate_credentials(username, password, request)
#
#     def authenticate_credentials(self, username, password, request=None):
#
#         if not username or username != "backkk":
#             raise exceptions.AuthenticationFailed("Invalid username")
#
#         if not password and password != 123456:
#             raise exceptions.AuthenticationFailed("Password is incorrect")


class SignUpUser(APIView):


    def post(self, request):
        if request.data.get("name") is None:
            return Response(data={"Should provide name of the user"}, status=422)
        if request.data.get("age") <= 18:
            return Response(data={"age should be greater than 18"}, status=422)
        if is_valid(request.data.get("email")) is None:
            return Response(data={"Enter valid email "}, status=422)
        elif request.data.get("email"):
            if is_valid(request.data.get("email")) is False:
                return Response(data={"Enter valid address"}, status=422)
        if request.data.get("password") is None:
            return Response(data={"Enter  email address"}, status=422)
        if request.data.get("designation") is None:
            return Response(data={"You must tell your designation before signup"}, status=422)
        password = request.data.get("password")
        password = make_password(password)
        user = User.objects.create(
                name=request.data.get("name"),
                age=request.data.get("age"),
                email=request.data.get("email"),
                password=password,
                address=request.data.get("address", "China"),
                is_active=True,
                date_joined=datetime.now(),
                last_login=datetime.now(),
                designation=request.data.get("designation")
        )
        return Response(data= {f" user created successfully and its id is  {user.id}"}, status=200)
