from apps.inicio.models import Paramsist


def paramsist_processors(request):
    fb_url = Paramsist.ObtenerValor("URL_FACEBOOK")
    logo = Paramsist.ObtenerValor("LOGO")
    whatsapp = Paramsist.ObtenerValor("WHATSAPP")
    whatsapp_link = whatsapp.replace("+","").replace("-","").replace(" ", "")
    email = Paramsist.ObtenerValor("EMAIL")
    ig_url = Paramsist.ObtenerValor("URL_IG")
    url_consulta_wsp = "https://wa.me/{}?text=Hola%20desearia%20saber%20el%20precio%20de%20".format(
        whatsapp_link
    )
    return {
        'fb_url': fb_url,
        'logo': logo,
        'email': email,
        'whatsapp': whatsapp,
        'whatsapp_link': whatsapp_link,
        'ig_url': ig_url,
        'url_consulta_wsp': url_consulta_wsp
    }