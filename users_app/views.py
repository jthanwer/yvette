from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomUserCreationForm, LogInForm
from .models import Profil


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        envoi = True
        return redirect('home')

    return render(request, 'users_app/register.html', locals())


def connexion(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return render(request, 'mainapp/accueil.html', locals())
            else:
                error = True

    else:
        form = LogInForm()

    return render(request, 'users_app/login.html', locals())


# Logout
def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


# View to see the personal profile
@login_required
def my_profile(request):
    profile = request.user.profil

    return render(request, 'users_app/my_profile.html', locals())

