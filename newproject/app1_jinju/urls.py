from django.contrib import admin
from django.urls import path
from . import views

app_name = "app1_jinju"

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # path('<int:pk>/vote/', views.vote, name='vote'),
]