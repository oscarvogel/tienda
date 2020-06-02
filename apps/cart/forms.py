from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class':'',
            'value':'1'
        }
    ))
    color = forms.IntegerField(widget=forms.HiddenInput())
    size = forms.IntegerField(widget=forms.HiddenInput())
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)