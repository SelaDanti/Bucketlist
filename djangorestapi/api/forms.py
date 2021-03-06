"""api/forms.py"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreated(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=('username','email')

class CustomUserChanged(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields
        