from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'ML'

urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    # path('admin/', admin.site.urls),
    # path('', views.upload, name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)