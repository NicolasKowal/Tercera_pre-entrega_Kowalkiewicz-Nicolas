from django import forms

class DueñosAdd(forms.Form): #se crea el form para agregar dueños
    nombre = forms.CharField()
    apellido = forms.CharField()
    nombreMascota = forms.CharField()

class MascotasAdd(forms.Form):#se crea el form para agregar mascotas
    nombre = forms.CharField()
    tipo = forms.CharField()
    edad = forms.IntegerField()

class MascotasForm(forms.Form):#se crea el form para consultar la existencia de las mascotas
    nombre = forms.CharField()

class DonacionesForm(forms.Form):#se crea el form para agregar donaciones
    nombre = forms.CharField()
    cantidad = forms.FloatField()