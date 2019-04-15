from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = "registration"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.LoginView, name='login'),
    # path('login/<access_token>/', views.LoginView, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dd', views.LogoutView.as_view(), name='logout'),
]