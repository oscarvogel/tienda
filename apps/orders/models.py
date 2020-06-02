from django.db import models

# Create your models here.
from apps.productos.models import Articulos


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre', default='')
    last_name = models.CharField(max_length=50, verbose_name='Apellido', default='')
    email = models.EmailField(default='')
    address = models.CharField(max_length=250, verbose_name='Domicilio', default='')
    postal_code = models.CharField(max_length=20, verbose_name='Cod Post', default='')
    city = models.CharField(max_length=100, verbose_name='Ciudad')
    cel_no = models.CharField(max_length=100, verbose_name='Celular', default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    paid = models.BooleanField(default=False, verbose_name='Pagado')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

    def __str__(self):
        return 'Orden {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Orden')
    product = models.ForeignKey(Articulos, related_name='order_items', on_delete=models.CASCADE, verbose_name='Articulo')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Cantidad')

    class Meta:
        verbose_name = 'Item Orden'
        verbose_name_plural = 'Item Orden'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity