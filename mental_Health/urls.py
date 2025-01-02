# mental_Health/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nomanapp.urls')),  # Assurez-vous que ce fichier existe et est correctement configuré
]
