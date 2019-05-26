from django import forms
from .models import Colocation
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout, Row, Column, Fieldset, MultiWidgetField
from crispy_forms.bootstrap import TabHolder, Tab, Field, Div


class ColocationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ColocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Etape 1 - Informations',
                    Fieldset('<div class=\"my-2 text-center\">Informations</div>',
                             Field('intro', placeholder='Ecrivez ici une petite description de votre colocation... ',
                                   style='color: black;'),
                             Field('two_words', placeholder="Votre colocation en deux mots..."),
                             Field('pets', placeholder="Vos animaux domestiques"),
                             ),

                    Div(StrictButton('<span class="fas fa-chevron-right" ></span> Suivant',
                                     type='button',
                                     css_class='btn-info btnNext px-3'
                                     ),

                        css_class="offset-md-8 col-md-4 text-right my-1"
                        )

                    ),

                Tab('Etape 2 - Adresse',
                    Fieldset('<div class=\"my-2 text-center\">Adresse</div>',
                             css_class="my-3",
                             style="min-height: 46vh;"
                             ),

                    Div(StrictButton('Précédent <span class="fas fa-chevron-left" ></span>',
                                     type='button',
                                     css_class='btn-warning btnPrevious px-3'
                                     ),

                        StrictButton('<span class="fas fa-chevron-right" ></span> Suivant',
                                     type='button',
                                     css_class='btn-info btnNext px-3'
                                     ),

                        css_class="offset-md-4 col-md-8 text-right my-1"
                        )

                    ),

                Tab('Etape 3 - Sécurité',
                    Fieldset('<div class=\"my-2 text-center\">Adresse</div>',
                             css_class="my-3",
                             style="min-height: 46vh;"
                             ),

                    Div(StrictButton('Précédent <span class="fas fa-chevron-left" ></span>',
                                     type='button',
                                     css_class='btn bg-1 btnPrevious px-3'
                                     ),

                        StrictButton('<span class="fas fa-check" ></span> Valider',
                                     type='submit',
                                     css_class='btn bg-2 px-3'
                                     ),

                        css_class="offset-md-4 col-md-8 text-right my-1"
                        ),
                    ),

                css_class="my-5"
            )
        )

    class Meta:
        model = Colocation
        fields = ('intro',
                  'two_words',
                  'pets')


class FilterForm(forms.Form):
    city = forms.CharField(label='Ville', min_length=4, max_length=30)
    age = forms.IntegerField(label='Age moyen')

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Field('city'),
            Field('age')
        )
