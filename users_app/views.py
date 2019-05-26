from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse, reverse_lazy
from .forms import CustomUserCreationForm, CustomUserEditForm, LogInForm
from .models import User


# def register(request):
#     form = CustomUserCreationForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         user = authenticate(email=form.cleaned_data['email'],
#                             password=form.cleaned_data['password1'])
#         login(request, user)
#         return redirect('home')
#
#     return render(request, 'users_app/register.html', locals())


class RegisterClassView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users_app/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super(RegisterClassView, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return valid


class EditClassView(UpdateView):
    model = User
    template_name = 'mainapp/update_coloc.html'
    form_class = CustomUserEditForm

    def get_object(self, queryset=None):
        obj = super(EditClassView, self).get_object()
        if not obj == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy('detail_profile', kwargs={'pk': pk})
        return success_url


def connexion(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                error = True

    else:
        form = LogInForm()

    return render(request, 'users_app/login.html', locals())


@login_required
def deconnexion(request):
    """
    Logout
    """
    logout(request)
    return redirect(reverse(connexion))


def detail_profile(request, pk):
    """
    Display the requested profil
    """
    user = User.objects.get(pk=pk)
    return render(request, 'users_app/profile.html', locals())


@login_required
def update_profile(request, pk):
    if request.user == User.objects.get(pk=pk):
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'users_app/profile.html', locals())
    else:
        raise Http404


