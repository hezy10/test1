from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

from .serializer import UserSerializer,UserInfoSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserInfoView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class AseasView():
    pass

