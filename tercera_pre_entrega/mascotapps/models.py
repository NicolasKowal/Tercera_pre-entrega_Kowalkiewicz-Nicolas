from django.db import models

class Dueños(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    nombreMascota = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f'{self.nombre} es el dueño de {self.nombreMascota}'


class Mascotas(models.Model):
    nombre = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    edad = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f'{self.nombre} es un {self.tipo}'


class Donaciones(models.Model):
    nombre = models.CharField(max_length=15)
    cantidad = models.FloatField(default=0)
    def __str__(self) -> str:
        return f'{self.nombre} donó ${self.cantidad}'