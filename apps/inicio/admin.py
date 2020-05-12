from django.contrib import admin

# Register your models here.
from apps.inicio.models import Paramsist


class ParamsistAdmin(admin.ModelAdmin):
    list_display = ('parametro','valor','detalle')
    search_fields = ('parametro', 'valor')

admin.site.register(Paramsist, ParamsistAdmin)