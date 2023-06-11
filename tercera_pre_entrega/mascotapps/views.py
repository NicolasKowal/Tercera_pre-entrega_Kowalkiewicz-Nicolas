from django.shortcuts import render
from .models import Mascotas, Donaciones, Dueños
from .forms import MascotasForm, MascotasAdd, DonacionesForm, DueñosAdd, DueñosForm

def index(request):
    return render(request, 'mascotapps/index.html')

def donaciones(request):
    if request.method == "POST":
        miFormulario = DonacionesForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            datos = Donaciones.objects.all()
            formu = Donaciones(nombre = informacion["nombre"], cantidad = informacion["cantidad"])
            formu.save()
            return render(request, "mascotapps/lista_donaciones.html", {'datos': datos})
    else:
        miFormulario = DonacionesForm()

    return render(request, "mascotapps/donaciones.html", {"miFormulario": miFormulario})

def buscar_mascotas(request):
    if request.method == 'POST':
        buscardatos = MascotasForm(request.POST)

        if buscardatos.is_valid():
            info = buscardatos.cleaned_data
            nombre = info['nombre']
            datos = Mascotas.objects.filter(nombre__icontains = nombre)
            if datos:
                return render(request, 'mascotapps/lista.html', {"datos": datos})
            else:
                mensaje = "No se encontraron mascotas con ese nombre"
                return render(request, 'mascotapps/buscardatos.html', {"buscardatos": buscardatos, "mensaje": mensaje})

    else:
        buscardatos = MascotasForm()
        return render(request, 'mascotapps/buscardatos.html', {"buscardatos": buscardatos})


def agregar_mascotas(request):
    if request.method == "POST":
        miFormulario = MascotasAdd(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            formu = Mascotas(nombre = informacion["nombre"], tipo = informacion["tipo"], edad = informacion["edad"])
            formu.save()
            return render(request, "mascotapps/main.html")
    else:
        miFormulario = MascotasAdd()

    return render(request, "mascotapps/mascota_add.html", {"miFormulario": miFormulario})

def agregar_dueños(request):
    if request.method == "POST":
        miFormulario = DueñosAdd(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            datos = Dueños.objects.all()
            formu = Dueños(nombre = informacion["nombre"], apellido = informacion["apellido"], nombreMascota = informacion["nombreMascota"])
            formu.save()
            return render(request, "mascotapps/lista_dueños.html", {'datos': datos})
    else:
        miFormulario = DueñosAdd()

    return render(request, "mascotapps/dueños.html", {"miFormulario": miFormulario})

def mostrar_dueños(request):
    datos = Dueños.objects.all()
    return render(request, 'mascotapps/lista_dueños.html', {"datos" : datos})

def main(request):
    return render(request, 'mascotapps/pagina_principal.html')