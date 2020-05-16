from django.urls import path

from apps.usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.login_propio, name='login'),
    path('logout/', views.user_logout, name='logout'),
]