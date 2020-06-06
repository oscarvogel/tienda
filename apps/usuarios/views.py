from os.path import join

from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from apps.inicio.models import Paramsist
from apps.usuarios.forms import SignUpForm
from apps.usuarios.tokens import account_activation_token


def login_propio(request):
    template = join(Paramsist.ObtenerValor("CARPETA_TEMA"), "usuarios", "login.html")
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                do_login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Contraseña o usuario no valido. Verifique!!!")
        else:
            print(form.errors)

    # Si llegamos al final renderizamos el formulario
    return render(request, template, {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            # current_site = get_current_site(request)
            # subject = 'Activa tu cuenta de Luly Shop'
            # message = render_to_string('fashion/usuarios/account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # user.email_user(subject, message)
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'fashion/usuarios/register.html', context={
        'form': form
    })

def account_activation_sent(request):
    return render(request, 'fashion/usuarios/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'fashion/usuarios/account_activation_invalid.html')