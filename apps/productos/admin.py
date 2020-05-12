from django.contrib import admin

# Register your models here.


from apps.productos.models import Articulos, Stock, Grupos

admin.site.site_header = 'Administracion de tablas Tienda'

class GrupoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    model = Grupos

class StockAdminInline(admin.TabularInline):
    model = Stock
    fields = ['idtalle', 'idcolor', 'stock', 'visible']

class ArticulosAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ('nombre','idgrupo__nombre')
    list_display = ('idarticulo','nombre','preciopub', 'idgrupo')
    list_editable = ('nombre', 'preciopub')
    list_filter = ['idgrupo',]
    inlines = [StockAdminInline,]

admin.site.register(Grupos, GrupoAdmin)
admin.site.register(Articulos, ArticulosAdmin)
