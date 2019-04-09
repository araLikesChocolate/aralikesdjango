from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = "registration"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/naver/', views.naver_callback, name='naver_callback'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]