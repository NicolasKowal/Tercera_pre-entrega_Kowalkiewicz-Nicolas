from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('mascotapps.urls')), #se llama al urls.py de la aplicacion mascotapps
]