from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ColocationForm
from .models import Colocation


def home(request):
    return render(request, 'mainapp/accueil.html')


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
