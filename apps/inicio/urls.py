from django.urls import path

from apps.inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]