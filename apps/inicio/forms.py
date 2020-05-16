from django import forms


class SearchForm(forms.Form):
    search_field = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Que buscas?'}
    ))