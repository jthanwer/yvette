from django import forms
from .models import User
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from bootstrap_datepicker_plus import DatePickerInput
from crispy_forms.layout import Layout, Row, Column, Fieldset, MultiWidgetField
from crispy_forms.bootstrap import TabHolder, Tab, Field, Div, InlineRadios

MONTHS = {
    1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
    5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
    9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
}


class CustomUserCreationForm(forms.Form):
    first_name = forms.CharField(label='Prénom', min_length=4, max_length=30)
    last_name = forms.CharField(label='Nom', min_length=4, max_length=30)
    email = forms.EmailField(label='Adresse e-mail')
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Mot de passe (confirmation)', widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1900, 1970), months=MONTHS)
    )
    city = forms.CharField(label='Ville')
    photo = forms.ImageField(label='Photo de profil', required=False)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].label = "%s" % "Date de naissance"
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Etape 1 - Identité',
                    Fieldset('<div class=\"my-2 text-center\">Identité</div>',
                             Field('first_name', placeholder='Ton prénom', style='color: black;'),
                             Field('last_name', placeholder="Ton nom de famille", css_class='text-success'),
                             Field('email', placeholder="email@example.com", css_class='text-success'),
                             MultiWidgetField('birth_date',
                                              attrs=(
                                              {'style': 'width: 30%; display: inline-block; margin-right: 3%;'}), ),
                             css_class="my-3",
                             style="min-height: 46vh;"
                             ),

                    Div(StrictButton('<span class="fas fa-chevron-right" ></span>',
                                     type='button',
                                     css_class='btn-info btnNext'
                                     ),
                        css_class="offset-md-8 col-md-4 text-right my-1"
                        )

                    ),

                Tab('Etape 2 - Adresse',
                    Fieldset('<div class=\"my-2 text-center\">Adresse</div>',
                             Field('city', placeholder='Ta ville', style='color: black;'),
                             css_class="my-3",
                             style="min-height: 46vh;"
                             ),

                    Div(StrictButton('<span class="fas fa-chevron-left" ></span>',
                                     type='button',
                                     css_class='btn-warning btnPrevious'
                                     ),

                        StrictButton('<span class="fas fa-chevron-right" ></span>',
                                     type='button',
                                     css_class='btn-info btnNext'
                                     ),

                        css_class="offset-md-4 col-md-8 text-right my-1"
                        )

                    ),

                Tab('Etape 3 - Sécurité',
                    Fieldset('<div class=\"my-2 text-center\">Sécurité</div>',
                             Field('password1', placeholder='Mot de passe', style='color: black;'),
                             Field('password2', placeholder='Confirmation de mot de passe', style='color: black;'),
                             css_class="my-3",
                             style="min-height: 46vh;"
                             ),

                    Div(StrictButton('<span class="fas fa-chevron-left" ></span>',
                                     type='button',
                                     css_class='btn-warning btnPrevious'
                                     ),

                        StrictButton('<span class="fas fa-check" ></span>',
                                     type='submit',
                                     css_class='btn-success'
                                     ),

                        css_class="offset-md-4 col-md-8 text-right my-1"
                        ),
                    ),

                css_class="my-5"
            )
        )

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
        user = User.objects.create_user(email=self.cleaned_data['email'],
                                        first_name=self.cleaned_data['first_name'],
                                        last_name=self.cleaned_data['last_name'],
                                        password=self.cleaned_data['password1'],
                                        birth_date=self.cleaned_data['birth_date'],
                                        city=self.cleaned_data['city'])
        print(user)
        user.save()
        return user


class LogInForm(forms.Form):
    email = forms.EmailField(label='Adresse e-mail')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
