from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'api'

urlpatterns = [
    path('delete/', views.deleteView, name='delete'),
    path('insert/', views.insertView, name='insert'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
