from django.contrib import admin

# Register your models here.


from apps.productos.models import Articulos, Stock, Grupos, ImagenArticulo, Color

admin.site.site_header = 'Administracion de tablas Tienda'

class ColoresAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['nombre']
    list_display = ['idcolor', 'nombre']
    list_editable = ['nombre']

class GrupoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    model = Grupos

class StockAdminInline(admin.TabularInline):
    model = Stock
    fields = ['idtalle', 'idcolor', 'stock', ]

class StockAdmin(admin.ModelAdmin):
    list_display = ['idarticulo', 'idcolor', 'idtalle', 'stock']
    list_per_page = 20
    search_fields = ['idarticulo__nombre']
    list_editable = ['stock']

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
    exclude = ['nombreticket', 'peso', 'tipoiva', 'descstock',]

admin.site.register(Grupos, GrupoAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Color, ColoresAdmin)
admin.site.register(Stock, StockAdmin)