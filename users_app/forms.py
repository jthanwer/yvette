from django import forms
from .models import User
from .layout import *
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate, logout
from crispy_forms.helper import FormHelper

MONTHS = {
    1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
    5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
    9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
}

# =========================
# =========================
# =========================


class CustomUserCreationForm(forms.ModelForm):
    """
    Form to register
    """
    password2 = forms.CharField(label='Mot de passe (confirmation)', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].label = "%s" % "Date de naissance"
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = layout_create_user

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Cet e-mail est déjà utilisé")
        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError("Les mots de passe ne correspondent pas")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(email=self.cleaned_data['email'],
                                        first_name=self.cleaned_data['first_name'],
                                        last_name=self.cleaned_data['last_name'],
                                        password=self.cleaned_data['password'],
                                        birth_date=self.cleaned_data['birth_date'],
                                        city=self.cleaned_data['city'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birth_date', 'city', 'password')
        widgets = {'birth_date': forms.SelectDateWidget(years=range(1900, 1970), months=MONTHS)}


# =========================
# =========================
# =========================


class CustomUserEditForm(forms.ModelForm):
    """
    Form to edit User account
    """

    def __init__(self, *args, **kwargs):
        super(CustomUserEditForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].label = "%s" % "Date de naissance"
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = layout_edit_user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'city')
        widgets = {'birth_date': forms.SelectDateWidget(years=range(1900, 1970), months=MONTHS)}

# =========================
# =========================
# =========================


class LogInForm(forms.Form):
    """
    Form to login
    """
    email = forms.EmailField(label='Adresse e-mail')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = layout_login

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if not r.count():
            raise ValidationError('Cet e-mail n\'est pas enregistré dans notre base de données')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        try:
            email = self.cleaned_data['email'].lower()
            if not authenticate(email=email, password=password):
                raise ValidationError('Le mot de passe est invalide')
        except KeyError:
            pass
        return password

