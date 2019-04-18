from django.urls import path
from .views import gTTs

app_name = 'gTTS'

urlpatterns = [
    path('<language>/<text>', gTTs),
]