from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Informar un correo valido.',
                             label='Correo Electronico')

    class Meta:
        model = User
        fields = ('username','password1', 'password2', 'email',)