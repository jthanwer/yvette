from django import forms
from .models import Profil, Colocation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Pseudonyme', min_length=4, max_length=150)
    first_name = forms.CharField(label='Prénom', min_length=4, max_length=30)
    last_name = forms.CharField(label='Nom', min_length=4, max_length=30)
    email = forms.EmailField(label='Adresse e-mail')
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Mot de passe (encore)', widget=forms.PasswordInput)
    age = forms.IntegerField(label='Age')
    city = forms.CharField(label='Ville')

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Ce pseudonyme existe déjà")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Cet e-mail est déjà utilisé")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Les mots de passe ne correspondent pas")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'])

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profil = Profil(user=user,
                        age=self.cleaned_data['age'],
                        city=self.cleaned_data['city'])
        profil.save()
        return profil


class LogInForm(forms.Form):
    username = forms.CharField(label='Pseudonyme', min_length=4, max_length=150)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)


class ColocationForm(forms.ModelForm):
    class Meta:
        model = Colocation
        fields = ('intro',
                  'two_words',
                  'pets')


