"""
URL configuration for tercera_pre_entrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from mascotapps import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('Donaciones/', views.donaciones, name = 'donaciones'),
    path('Buscar_Mascotas/', views.buscar_mascotas, name = 'buscar'),
    path('Agregar_Mascotas/', views.agregar_mascotas, name = 'agregar'),
    path('Dueños/', views.mostrar_dueños, name= 'dueños'), 
    path('Dueños_add/', views.agregar_dueños, name= 'agregar-dueños'), 
    
]
