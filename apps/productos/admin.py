from django.contrib import admin

# Register your models here.
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from apps.productos.models import Articulos, Stock, Grupos, ImagenArticulo, Color, Marcas

admin.site.site_header = 'Administracion de tablas Tienda'

class MarcasAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['nombre']
    list_display = ['idmarca', 'nombre', 'habilita_web']
    list_editable = ['nombre', 'habilita_web']

class ColoresAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['nombre']
    list_display = ['idcolor', 'nombre', 'color_web']
    list_editable = ['nombre', 'color_web']
    exclude = ['color']

class GrupoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_per_page = 20
    list_display = ['idgrupo', 'nombre', 'habilita_web']
    list_editable = ['nombre', 'habilita_web']

class StockAdminInline(admin.TabularInline):
    model = Stock
    fields = ['idtalle', 'idcolor', 'stock', 'preciopub']

class StockAdmin(admin.ModelAdmin):
    list_display = ['idarticulo', 'idcolor', 'idtalle', 'stock', 'preciopub']
    list_per_page = 20
    search_fields = ['idarticulo__nombre', 'idarticulo__etiqueta']
    list_editable = ['stock', 'preciopub']

class ImagenProductoInLine(admin.StackedInline):
    model = ImagenArticulo
    fields = ['imagen', 'imagen_tag', 'principal']
    readonly_fields = ['imagen_tag']

class ArticulosAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ('nombre', 'idgrupo__nombre', 'etiqueta')
    list_display = ('idarticulo','nombre','preciopub', 'disponible_web', 'etiqueta')
    list_editable = ('nombre', 'preciopub','disponible_web', 'etiqueta')
    list_filter = (
        ('idgrupo', RelatedDropdownFilter),
        ('idmarca', RelatedDropdownFilter),
        'disponible_web'
    )
    inlines = [StockAdminInline, ImagenProductoInLine]
    exclude = ['nombreticket', 'peso', 'tipoiva', 'descstock', 'ult_act', 'favoritos']

admin.site.register(Grupos, GrupoAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Color, ColoresAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Marcas, MarcasAdmin)