from django.contrib import admin

# Register your models here.
from apps.inicio.models import Paramsist, Secciones, DetalleSecciones


class ParamsistAdmin(admin.ModelAdmin):
    list_display = ('parametro','valor','detalle')
    search_fields = ('parametro', 'valor')

class DetalleSeccionesInLine(admin.StackedInline):
    model = DetalleSecciones
    fields = ['titulo', 'imagen', 'imagen_tag', 'detalle', 'articulo']
    readonly_fields = ['imagen_tag']

class SeccionesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_seccion')
    search_fields = ('nombre',)
    inlines = [DetalleSeccionesInLine]

admin.site.register(Paramsist, ParamsistAdmin)
admin.site.register(Secciones, SeccionesAdmin)