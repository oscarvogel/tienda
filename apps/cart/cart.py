from decimal import Decimal

from django.conf import settings

from apps.productos.models import Articulos


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        #si no existe la sesion la creo
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    """
    product es una instancia de la clase producto
    quantity es la cantidad a agregar (puede ser negativo)
    update_quantity indica si estoy actualizando la cantidad o estoy estableciendo la cantidad
    """
    def add(self, product, quantity=1, update_quantity=False):
        """
         Add a product to the cart or update its quantity.
         Convertimos el ID del producto en una cadena porque Django usa JSON para serializar los datos de la sesión,
         y JSON solo permite nombres de clave de cadena
         """
        product_id = str(product.idarticulo)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.preciopub)}

        #si se esta actualizando la cantidad la sumo
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.idarticulo)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Articulos.objects.filter(idarticulo__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.idarticulo)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    #obtener el total de la compra
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
