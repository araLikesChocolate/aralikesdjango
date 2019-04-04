from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "registration"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # path('<int:pk>/vote/', views.vote, name='vote'),
]