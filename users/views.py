from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions

from users.serializers import UserSerializer

# Create your views here.


class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
