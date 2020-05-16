from os.path import join

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login

# Create your views here.
from apps.inicio.models import Paramsist


def login_propio(request):
    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "usuarios", "login.html")
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
                do_login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Contraseña o usuario no valido. Verifique!!!")
        else:
            for e in form.error_messages:
                messages.error(request, e)

    # Si llegamos al final renderizamos el formulario
    return render(request, template, {'form': form})

