from os.path import join

from django.shortcuts import render
# Create your views here.
from apps.inicio.forms import SearchForm, CategoriasForm
from apps.inicio.models import Paramsist, Secciones
from apps.productos.models import Articulos, Historial


def inicio(request):
    form_busqueda = SearchForm()
    form_categoria = CategoriasForm()
    categorias_articulos = Paramsist.ObtenerValor('CATEGORIA_HOMBRES')
    if categorias_articulos:
        articulos_hombres = Articulos.objects.filter(
            idgrupo__in=[x for x in categorias_articulos.split(',')],
            disponible_web = True
        ).order_by('-ult_act')[:8]
    else:
        articulos_hombres = None

    categorias_articulos = Paramsist.ObtenerValor('CATEGORIA_MUJERES')
    if categorias_articulos:
        articulos_mujeres = Articulos.objects.filter(
            idgrupo__in=[x for x in categorias_articulos.split(',')],
            disponible_web = True
        ).order_by('-ult_act')[:8]
    else:
        articulos_mujeres = None

    categorias_articulos = Paramsist.ObtenerValor('CATEGORIA_DEPORTES')
    if categorias_articulos:
        articulos_deportes = Articulos.objects.filter(
            idgrupo__in=[x for x in categorias_articulos.split(',')],
            disponible_web = True
        ).order_by('-ult_act')[:8]
    else:
        articulos_deportes = None

    categorias_articulos = Paramsist.ObtenerValor('CATEGORIA_CALZADOS')
    if categorias_articulos:
        articulos_calzados = Articulos.objects.filter(
            idgrupo__in=[x for x in categorias_articulos.split(',')],
            disponible_web = True
        ).order_by('-ult_act')[:8]
    else:
        articulos_calzados = None

    articulos = None
    historial = None

    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "index.html")
    if request.user.is_authenticated:
        historial = Historial.objects.filter(usuario = request.user).order_by('-fecha')[:10]

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
    try:
        ofertas = Secciones.objects.get(tipo_seccion = 'OF')
    except:
        ofertas = None
    return render(request, template_name=template, context={
        'hero': hero,
        'banner_1': banner_1,
        'banner_2': banner_2,
        'articulos': articulos,
        'form': form_busqueda,
        'ofertas': ofertas,
        'historial': historial,
        'form_categoria': form_categoria,
        'articulos_hombres': articulos_hombres,
        'articulos_mujeres': articulos_mujeres,
        'articulos_deportes': articulos_deportes,
        'articulos_calzados': articulos_calzados
    })

