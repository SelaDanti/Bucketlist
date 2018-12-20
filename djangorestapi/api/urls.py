"""api/urls.py"""
from django.urls import path , include
from rest_framework import routers
from . import views

all_users=routers.DefaultRouter()
all_users.register('',views.UserListView)
urlpatterns = [
    
    path('items/', views.CreateView.as_view(), name="create"),
    path('', include(all_users.urls))
]