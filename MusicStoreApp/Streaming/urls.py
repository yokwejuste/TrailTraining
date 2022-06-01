from django.urls import path
from Streaming.views import *


urlpatterns = [
    path('', home, name='home')
]
