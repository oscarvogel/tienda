from django.urls import path

from apps.productos import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto>', views.get_producto, name='get_producto'),
]