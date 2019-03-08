from django import forms
from .models import Profil, Colocation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ColocationForm(forms.ModelForm):
    class Meta:
        model = Colocation
        fields = ('intro',
                  'two_words',
                  'pets')


