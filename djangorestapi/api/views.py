"""api/views"""
from rest_framework import generics, viewsets
from . import models
from . import serializers


class UserListView(viewsets.ModelViewSet):
    queryset=models.CustomUser.objects.all()
    serializer_class=serializers.UserSerializer

    