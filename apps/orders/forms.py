from django import forms

from apps.orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                'postal_code', 'city', 'cel_no']
