from django.urls import path, include

from .views import trilhas


urlpatterns = [
    path('', trilhas, name='trilhas'),
]