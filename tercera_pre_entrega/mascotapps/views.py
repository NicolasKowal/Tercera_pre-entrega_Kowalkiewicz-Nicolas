from django.shortcuts import render
from .models import Mascotas, Donaciones, Dueños
from .forms import MascotasForm, MascotasAdd, DonacionesForm, DueñosAdd

def index(request):
    return render(request, 'mascotapps/index.html')

def donaciones(request):
    if request.method == "POST":
        miFormulario = DonacionesForm(request.POST) #se crea un formulario

        if miFormulario.is_valid(): #validacion de datos
            informacion = miFormulario.cleaned_data
            datos = Donaciones.objects.all() #se guardan todos los objetos de la clase donaciones en la variable datos
            formu = Donaciones(nombre = informacion["nombre"], cantidad = informacion["cantidad"]) #se crea un objeto de la clase donaciones
            formu.save() #se guarda el objeto
            return render(request, "mascotapps/lista_donaciones.html", {'datos': datos}) #se retorna la web lista_donaciones y se le pasa la variable como diccionario de datos
    else:
        miFormulario = DonacionesForm() #si la solicitud es get, se crea un formulario 
    return render(request, "mascotapps/donaciones.html", {"miFormulario": miFormulario}) #se retorna la web donaciones y se le pasa el formulario como variable

def buscar_mascotas(request):
    if request.method == 'POST':
        buscardatos = MascotasForm(request.POST)#se crea una instancia
        if buscardatos.is_valid():#validacion de datos
            info = buscardatos.cleaned_data #se obtienen datos limpios del formulario
            nombre = info['nombre'] #se guarda en nombre la informacion de info[nombre]
            datos = Mascotas.objects.filter(nombre__icontains = nombre) #se guarda en datos los objetos de la clase mascotas que coincida con el nombre
            if datos:
                return render(request, 'mascotapps/lista.html', {"datos": datos}) #si datos es verdadero, se muestran
            else:
                mensaje = "No se encontraron mascotas con ese nombre"
                return render(request, 'mascotapps/buscardatos.html', {"buscardatos": buscardatos, "mensaje": mensaje}) #si no se encuentra el dato, se muestra el mensaje que no se encontraron
    else:
        buscardatos = MascotasForm()#si la solicitud es get, se crea un formulario 
        return render(request, 'mascotapps/buscardatos.html', {"buscardatos": buscardatos}) #se muestra la pagina buscardatos con el formulario

def agregar_mascotas(request):
    if request.method == "POST":
        miFormulario = MascotasAdd(request.POST)#se crea una instancia
        if miFormulario.is_valid():#validacion de datos
            informacion = miFormulario.cleaned_data#se obtienen datos limpios del formulario
            formu = Mascotas(nombre = informacion["nombre"], tipo = informacion["tipo"], edad = informacion["edad"])#se crea un objeto de la clase mascotas con los parametros de la isntancia anterior
            formu.save() #se guarda el objeto
            return render(request, "mascotapps/main.html") #te devuelve al mail
    else:
        miFormulario = MascotasAdd()#si la solicitud es get, se crea un formulario 
    return render(request, "mascotapps/mascota_add.html", {"miFormulario": miFormulario})#se muestra la pagina mascota_Add con el formulario

def agregar_dueños(request):
    if request.method == "POST":
        miFormulario = DueñosAdd(request.POST)#se crea una instancia
        if miFormulario.is_valid():#validacion de datos
            informacion = miFormulario.cleaned_data#se obtienen datos limpios del formulario
            datos = Dueños.objects.all() #se obtienen todos los objetos de la clase dueños para mostrarlos a continuacion
            formu = Dueños(nombre = informacion["nombre"], apellido = informacion["apellido"], nombreMascota = informacion["nombreMascota"])
            formu.save()
            return render(request, "mascotapps/lista_dueños.html", {'datos': datos})
    else:
        miFormulario = DueñosAdd()
    return render(request, "mascotapps/dueños.html", {"miFormulario": miFormulario})

def mostrar_dueños(request):
    datos = Dueños.objects.all() #se obtienen todos los objetos de dueños y se la guarda en datos, para mostrarlos a continuacion
    return render(request, 'mascotapps/lista_dueños.html', {"datos" : datos})

def main(request):
    return render(request, 'mascotapps/pagina_principal.html')#muestra la pagina main