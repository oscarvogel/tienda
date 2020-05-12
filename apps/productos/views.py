from os.path import join

from django.shortcuts import render

# Create your views here.
from apps.inicio.models import Paramsist


def lista_productos(request):
    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"),"productos", "lista_productos.html")
    return render(request, template_name=template)