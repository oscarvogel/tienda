from os.path import join

from django.shortcuts import render
# Create your views here.
from apps.inicio.forms import SearchForm, CategoriasForm
from apps.inicio.models import Paramsist, Secciones
from apps.productos.models import Articulos, Historial


def inicio(request):
    form_busqueda = SearchForm()
    form_categoria = CategoriasForm()
    articulos = None
    historial = None
    # # if request.method == 'POST':
    # #     form_busqueda = SearchForm(request.POST)
    # #     if form_busqueda.is_valid():
    # #         cd = form_busqueda.cleaned_data
    # #         articulos = Articulos.objects.filter(nombre__icontains = cd['search_field'], disponible_web = True)
    # #         template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "productos", "lista_productos.html")
    # # else:
    #     template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "index.html")

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
    })

