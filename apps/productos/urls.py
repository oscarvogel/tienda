from django.urls import path, include
from rest_framework import routers

from apps.productos import views

app_name = 'productos'
router = routers.DefaultRouter()

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('/<int:categoria_id>', views.lista_productos, name='lista_producto_categoria'),
    path('producto/<int:producto>', views.get_producto, name='get_producto'),
    path('favoritos/', views.favorito_articulo, name='favorito_articulo'),
    path('api/v1.0/', include(router.urls)),
]