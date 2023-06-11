from django.contrib import admin
from .models import Dueños, Mascotas, Donaciones

#se agregan al admin las 3 bases de datos siguientes para editarlas

admin.site.register(Dueños)
admin.site.register(Mascotas)
admin.site.register(Donaciones)