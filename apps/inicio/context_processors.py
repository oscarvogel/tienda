from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from apps.inicio.models import Paramsist
from apps.productos.models import Grupos, Marcas


def paramsist_processors(request):
    url_web = Paramsist.ObtenerValor("URL_WEB")
    fb_url = Paramsist.ObtenerValor("URL_FACEBOOK")
    logo = Paramsist.ObtenerValor("LOGO")
    whatsapp = Paramsist.ObtenerValor("WHATSAPP")
    whatsapp_link = whatsapp.replace("+","").replace("-","").replace(" ", "")
    email = Paramsist.ObtenerValor("EMAIL")
    ig_url = Paramsist.ObtenerValor("URL_IG")
    url_consulta_wsp = "https://wa.me/{}?text=Hola%20desearia%20saber%20el%20precio%20de%20".format(
        whatsapp_link
    )
    categorias = Grupos.objects.filter(habilita_web = True)
    marcas = Marcas.objects.filter(habilita_web = True).order_by('nombre')
    try:
        favoritos_usuario = User.objects.get(username=request.user).fav_user.count()
    except:
        favoritos_usuario = 0
    form_usuario = AuthenticationForm()

    categorias_articulos = Paramsist.ObtenerValor('CATEGORIA_HOMBRES')
    if categorias_articulos:
        categorias_hombres = Grupos.objects.filter(
            idgrupo__in=[x for x in categorias_articulos.split(',')],
            habilita_web = True
        )
    else:
        categorias_hombres = None

    categorias_articulos = Paramsist.ObtenerValor('CATEGORIA_MUJERES')
    if categorias_articulos:
        categorias_mujeres = Grupos.objects.filter(
            idgrupo__in=[x for x in categorias_articulos.split(',')],
            habilita_web = True
        )
    else:
        categorias_mujeres = None

    return {
        'url_web':url_web,
        'fb_url': fb_url,
        'logo': logo,
        'email': email,
        'whatsapp': whatsapp,
        'whatsapp_link': whatsapp_link,
        'ig_url': ig_url,
        'url_consulta_wsp': url_consulta_wsp,
        'categorias': categorias,
        'marcas': marcas,
        'favoritos_usuario': favoritos_usuario,
        'form_usuario':form_usuario,
        'categorias_hombres':categorias_hombres,
        'categorias_mujeres':categorias_mujeres,
    }