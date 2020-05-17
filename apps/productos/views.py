from os.path import join

from django.shortcuts import render

# Create your views here.
from apps.inicio.models import Paramsist
from apps.productos.models import Articulos, Historial


def lista_productos(request):
    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"),"productos", "lista_productos.html")
    return render(request, template_name=template)

def get_producto(request, producto=1):

    articulo = Articulos.objects.get(idarticulo=producto)
    if request.user.is_authenticated:
        historial = Historial()
        historial.usuario = request.user
        historial.articulo = articulo
        historial.save()

    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "productos", "producto_invididual.html")
    return render(request, template_name=template, context={
        'articulo': articulo
    })