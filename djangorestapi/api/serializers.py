#api/serializers.py

from rest_framework import serializers
from .models import ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    """Serializer will convert Model input to JSON format."""
    class Meta:
        """Meta class will map serializer field with the models fileds."""
        model=ToDoList
        fields=('id','item_name','date_created','date_modified','compelete')
        read_only_field=('date_created', 'date_modified')