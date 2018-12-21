"""authapi/urls.py"""
from django.urls import path , include

urlpatterns = [
    path('users/', include('api.urls')),
    # login route http://127.0.0.1:8000/api/rest-auth/login/
    path('rest-auth/', include('rest_auth.urls')),
]
