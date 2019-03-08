from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ColocationForm, CustomUserCreationForm, LogInForm
from .models import Colocation


def home(request):
    return render(request, 'mainapp/accueil.html')


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        envoi = True
        return redirect('home')

    return render(request, 'mainapp/register.html', locals())


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

    return render(request, 'mainapp/login.html', locals())


# Logout
def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


# View to see the personal profile
@login_required
def my_profile(request):
    profile = request.user.profil

    return render(request, 'mainapp/my_profile.html', locals())


# View to create a new colocation
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

    return render(request, 'mainapp/new_coloc.html', locals())


def scroll_colocs(request):
    colocations = Colocation.objects.all()
    return render(request, 'mainapp/colocations.html', {'colocations': colocations})


def discover_a_coloc(request, id):
    colocations = Colocation.objects.all()
    return render(request, 'mainapp/colocations.html', {'colocations': colocations})
