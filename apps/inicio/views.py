from os.path import join

from django.shortcuts import render
# Create your views here.
from apps.inicio.models import Paramsist, Secciones


def inicio(request):
    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "index.html")
    try:
        hero = Secciones.objects.get(tipo_seccion = 'B2', activo=True)
    except:
        hero = None
    try:
        banner_1 = Secciones.objects.get(tipo_seccion = 'S1')
    except:
        banner_1 = None
    try:
        banner_2 = Secciones.objects.get(tipo_seccion = 'S2')
    except:
        banner_2 = None

    return render(request, template_name=template, context={
        'hero': hero,
        'banner_1': banner_1,
        'banner_2': banner_2,
    })

