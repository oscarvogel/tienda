from django.urls import path

from apps.inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cuentas/', views.login_propio, name='login_propio'),
]