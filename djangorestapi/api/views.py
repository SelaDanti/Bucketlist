# api/views.py

from rest_framework import generics, viewsets
from . import models
from . import serializers
from django.shortcuts import render


class UserListView(viewsets.ModelViewSet):
    queryset=models.CustomUser.objects.all()
    serializer_class=serializers.UserSerializer

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.ToDoList.objects.all()
    serializer_class = serializers.ToDoListSerializer

    def perform_create(self, serializer):
        """Save new item."""
        serializer.save()  