from django import forms

from apps.productos.models import Grupos, Marcas


class SearchForm(forms.Form):
    search_field = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Que buscas?'}
    ), required=False)
    marcas = forms.ModelChoiceField(
        required=False,
        queryset=Marcas.objects.filter(habilita_web = True).order_by('nombre'), widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'bc-item'
            }
        )
    )

class CategoriasForm(forms.Form):
    categoria = forms.ModelChoiceField(widget=forms.Select(
        attrs={'class': 'category-btn'}
    ), queryset=Grupos.objects.filter(habilita_web=True),
        required=False
    )
