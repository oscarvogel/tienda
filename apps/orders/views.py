from django.shortcuts import render

# Create your views here.
from apps.cart.cart import Cart
from apps.orders.forms import OrderCreateForm
from apps.orders.models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],
                                         quantity=item['quantity'])

                # clear the cart
            cart.clear()
            return render(request,'fashion/orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,'fashion/orders/order/check-out.html', {'cart': cart, 'form': form})