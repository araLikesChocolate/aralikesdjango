from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = "logout"

urlpatterns = [
    path('', views.logout, name='logout'),
]