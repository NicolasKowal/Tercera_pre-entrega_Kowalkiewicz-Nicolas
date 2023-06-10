from django import forms

class DueñosForm(forms.Form):
    nombre = forms.CharField()

class DueñosAdd(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    nombreMascota = forms.CharField()

class MascotasAdd(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()
    edad = forms.IntegerField()

class MascotasForm(forms.Form):
    nombre = forms.CharField()

class DonacionesForm(forms.Form):
    nombre = forms.CharField()
    cantidad = forms.FloatField()