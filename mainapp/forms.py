from django import forms
from .models import Colocation
from django.core.exceptions import ValidationError


class ColocationForm(forms.ModelForm):
    class Meta:
        model = Colocation
        fields = ('intro',
                  'two_words',
                  'pets')


