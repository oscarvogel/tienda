from os.path import join

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login
# Create your views here.
from apps.inicio.models import Paramsist, Secciones


def inicio(request):
    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "index.html")
    hero = Secciones.objects.get(tipo_seccion = 'B2')
    banner_1 = Secciones.objects.get(tipo_seccion = 'S2')
    return render(request, template_name=template, context={
        'hero': hero,
        'banner_1': banner_1,
    })

