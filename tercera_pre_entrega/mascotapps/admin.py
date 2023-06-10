from django.contrib import admin
from .models import Dueños, Mascotas, Donaciones

admin.site.register(Dueños)
admin.site.register(Mascotas)
admin.site.register(Donaciones)