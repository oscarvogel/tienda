from os.path import join

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login
# Create your views here.
from apps.inicio.models import Paramsist


def inicio(request):
    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "index.html")
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                #hacemos un login manual
                do_login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Contraseña o usuario no valido. Verifique!!!")
        else:
            print(f"Erorres formulario {form.errors}")
    return render(request, template_name=template, context={
        'form':form
    })

def login_propio(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                return redirect('/')
            else:
                messages.error(request, "Contraseña o usuario no valido. Verifique!!!")

    # Si llegamos al final renderizamos el formulario
    return render(request, "index.html", {'form': form})
