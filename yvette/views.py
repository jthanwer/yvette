from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ColocationForm, CustomUserCreationForm, LogInForm
from .models import Colocation


def home(request):
    return render(request, 'yvette/accueil.html')


def colocations(request):
    colocations = Colocation.objects.all()
    return render(request, 'yvette/colocations.html', {'colocations': colocations})


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        envoi = True
        return redirect('home')

    return render(request, 'yvette/register.html', locals())


def connexion(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return render(request, 'yvette/accueil.html', locals())
            else:
                error = True

    else:
        form = LogInForm()

    return render(request, 'yvette/login.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


@login_required
def create_coloc(request):
    if hasattr(request.user.profil, 'colocation'):
        already_coloc = True
    else:
        form = ColocationForm(request.POST or None)
        if form.is_valid():
            envoi = True
            coloc = form.save(commit=False)
            coloc.createur = request.user.profil
            coloc.mean_age = request.user.profil.age
            coloc.save()

    return render(request, 'yvette/new_coloc.html', locals())

