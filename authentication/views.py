from . import forms
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

# Vue générique
""" Ben ! rien du tout ici. La vue est déjà faite par Django.
    il suffit de faire sont implémentation dans url.py et setting.py
    https://docs.djangoproject.com/fr/3.1/topics/auth/default/#all-authentication-views
    https://ccbv.co.uk/
# ---"""


# Vue basée sur une classe
"""from django.views.generic import View

class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        message = ''
        return render(
            request, self.template_name, context={'form': self.form_class(), 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = f"Identifiants invalides !"  # {form.cleaned_data['password']}"
        return render(
            request, self.template_name, context={'form': form, 'message': message})
# ---"""


# Vue basée sur une fonction
"""def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = f"Identifiants invalides !" # {form.cleaned_data['password']}"
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})
#---"""


"""def logout_user(request):
    logout(request)
    return redirect('login')
#---"""

