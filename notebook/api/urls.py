from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# app_name = 'api'

urlpatterns = [
    path('', views.upload),
    path('delete/', views.deleteView),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
