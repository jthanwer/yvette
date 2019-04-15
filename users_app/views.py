from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomUserCreationForm, LogInForm
from .models import Profile



def register(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
        login(request, user)
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
                return redirect('home')
            else:
                error = True

    else:
        form = LogInForm()

    return render(request, 'users_app/login.html', locals())


# Logout
def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


# Display the personal profile
def detail_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    # profile = request.user.profile

    return render(request, 'users_app/profile.html', locals())

