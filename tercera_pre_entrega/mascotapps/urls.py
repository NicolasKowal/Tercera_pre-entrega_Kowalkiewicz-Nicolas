from django.urls import path
from mascotapps import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('Donaciones/', views.donaciones, name = 'donaciones'),
    path('Buscar_Mascotas/', views.buscar_mascotas, name = 'buscar'),
    path('Agregar_Mascotas/', views.agregar_mascotas, name = 'agregar'),
    path('Dueños/', views.mostrar_dueños, name= 'dueños'), 
    path('Dueños_add/', views.agregar_dueños, name= 'agregar-dueños'), 
    path('Pagina_principal', views.main, name ='main')
]
