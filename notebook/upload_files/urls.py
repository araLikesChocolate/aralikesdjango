from django.urls import path, include
from . import views

app_name = 'upload_files'

urlpatterns = [
    path('', views.file, name='file'),
    path('submit/', views.file_submit, name='file_submit'),    
    path('list/', views.DataListView.as_view(), name='file_list'),
    path('detail/<pk>/', views.DataDetailView.as_view(), name='file_detail'),
]