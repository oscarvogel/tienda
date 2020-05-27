from os.path import join

from django.shortcuts import render

from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
from apps.cart.forms import CartAddProductForm
from apps.inicio.forms import SearchForm, CategoriasForm
from apps.inicio.models import Paramsist
from apps.productos.models import Articulos, Historial


def lista_productos(request, categoria_id=0):
    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"),"productos", "lista_productos.html")
    form_busqueda = SearchForm()
    form_categoria = CategoriasForm()
    articulos = None
    historial = None

    if request.method == 'POST':
        form_busqueda = SearchForm(request.POST)
        form_categoria = CategoriasForm(request.POST)
        if form_busqueda.is_valid() and form_categoria.is_valid():
            cd = form_busqueda.cleaned_data
            cd_cat = form_categoria.cleaned_data
            print(cd_cat['categoria'])
            articulos = Articulos.objects.filter(nombre__icontains = cd['search_field'],
                                                 disponible_web = True,
                                                 idgrupo = cd_cat['categoria'])
            # print(articulos.query)
            template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "productos", "lista_productos.html")
    else:
        articulos = Articulos.objects.filter(idgrupo = categoria_id)

    if request.user.is_authenticated:
        historial = Historial.objects.filter(usuario = request.user).order_by('-fecha')[:10]

    return render(request, template_name=template, context={
        'articulos': articulos,
        'form': form_busqueda,
        'historial': historial,
        'form_categoria': form_categoria,
    })

def get_producto(request, producto=1):

    cart_product_form = CartAddProductForm()

    articulo = Articulos.objects.get(idarticulo=producto)
    if request.user.is_authenticated:
        historial = Historial()
        historial.usuario = request.user
        historial.articulo = articulo
        historial.save()

    relacionados = Articulos.objects.filter(idgrupo = articulo.idgrupo)[:4]

    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "productos", "producto_invididual.html")
    return render(request, template_name=template, context={
        'articulo': articulo,
        'relacionados': relacionados,
        'cart_product_form': cart_product_form,
    })

@login_required(login_url='usuarios:login')
@require_POST
def favorito_articulo(request):
    articulo_id = request.POST.get('idarticulo')
    action = request.POST.get('action')
    if articulo_id and action:
        try:
            articulo = Articulos.objects.get(idarticulo=articulo_id)
            if action == 'like':
                articulo.favoritos.add(request.user)
            else:
                articulo.favoritos.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ko'})