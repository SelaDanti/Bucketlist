"""api/admin.py"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser



class CustomAdmin(UserAdmin):
    user_form = UserCreationForm
    form=UserChangeForm
    model=CustomUser
    list_display=['email','username','name']


admin.site.register(CustomUser,CustomAdmin)

