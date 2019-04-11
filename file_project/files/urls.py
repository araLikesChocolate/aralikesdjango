from django.urls import path, include
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.file, name='file'),
    path('list/', views.DataListView.as_view(), name='list'),
]