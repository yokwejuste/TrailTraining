from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.co

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
