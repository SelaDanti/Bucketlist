#api/serializers.py
from rest_framework import serializers
from . import models
from .models import ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    """Serializer will convert Model input to JSON format."""
    class Meta:
        """Meta class will map serializer field with the models fileds."""
        model=ToDoList
        fields=('id','item_name','date_created','date_updated','complete')
        read_only_field=('date_created', 'date_modified')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields=('email','username',)