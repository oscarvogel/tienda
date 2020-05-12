from apps.inicio.models import Paramsist


def paramsist_processors(request):
    fb_url = Paramsist.ObtenerValor("URL_FACEBOOK")
    logo = Paramsist.ObtenerValor("LOGO")
    return {
        'fb_url': fb_url,
        'logo': logo,
    }