from django.contrib import admin

# Register your models here.


from apps.productos.models import Articulos, Stock, Grupos, ImagenArticulo

admin.site.site_header = 'Administracion de tablas Tienda'

class GrupoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    model = Grupos

class StockAdminInline(admin.TabularInline):
    model = Stock
    fields = ['idtalle', 'idcolor', 'stock', 'visible']

class ImagenProductoInLine(admin.StackedInline):
    model = ImagenArticulo
    fields = ['imagen', 'imagen_tag']
    readonly_fields = ['imagen_tag']

class ArticulosAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ('nombre','idgrupo__nombre')
    list_display = ('idarticulo','nombre','preciopub', 'idgrupo', 'disponible_web')
    list_editable = ('nombre', 'preciopub','disponible_web')
    list_filter = ['idgrupo',]
    inlines = [StockAdminInline, ImagenProductoInLine]
    exclude = ['nombreticket']

admin.site.register(Grupos, GrupoAdmin)
admin.site.register(Articulos, ArticulosAdmin)
