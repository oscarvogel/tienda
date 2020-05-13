from apps.inicio.models import Paramsist


def paramsist_processors(request):
    fb_url = Paramsist.ObtenerValor("URL_FACEBOOK")
    logo = Paramsist.ObtenerValor("LOGO")
    whatsapp = Paramsist.ObtenerValor("WHATSAPP")
    whatsapp_link = whatsapp.replace("+","").replace("-","").replace(" ", "")
    email = Paramsist.ObtenerValor("EMAIL")
    return {
        'fb_url': fb_url,
        'logo': logo,
        'email': email,
        'whatsapp': whatsapp,
        'whatsapp_link': whatsapp_link,
    }