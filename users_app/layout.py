from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout, Row, Column, Fieldset, MultiWidgetField
from crispy_forms.bootstrap import TabHolder, Tab, Field, Div


# =================================
# Layout for CustomUserCreationForm
# =================================

layout_create_user = Layout(
    TabHolder(
        Tab('Etape 1 - Identité',
            Fieldset('<div class=\"my-2 text-center\">Identité</div>',
                     Field('first_name', placeholder='Ton prénom', style='color: black;'),
                     Field('last_name', placeholder="Ton nom de famille"),
                     Field('email', placeholder="email@example.com"),
                     MultiWidgetField('birth_date',
                                      attrs=(
                                          {'style': 'width: 30%; display: inline-block; margin-right: 3%;'}), ),
                     css_class="my-3",
                     style="min-height: 46vh;"
                     ),

            Div(StrictButton('<span class="fas fa-chevron-right" ></span> Suivant',
                             type='button',
                             css_class='btn bg-2 btnNext px-3'
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

            Div(StrictButton('Précédent <span class="fas fa-chevron-left" ></span>',
                             type='button',
                             css_class='btn bg-1 btnPrevious px-3'
                             ),

                StrictButton('<span class="fas fa-chevron-right" ></span> Suivant',
                             type='button',
                             css_class='btn bg-2 btnNext px-3'
                             ),

                css_class="offset-md-4 col-md-8 text-right my-1"
                )

            ),

        Tab('Etape 3 - Sécurité',
            Fieldset('<div class=\"my-2 text-center\">Sécurité</div>',
                     Field('password', placeholder='Mot de passe', style='color: black;'),
                     Field('password2', placeholder='Confirmation de mot de passe', style='color: black;'),
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


# =================================
# Layout for EditUserForm
# =================================

layout_edit_user = Layout(
    TabHolder(
        Tab('Etape 1 - Identité',
            Fieldset('<div class=\"my-2 text-center\">Identité</div>',
                     Field('first_name', placeholder='Ton prénom', style='color: black;'),
                     Field('last_name', placeholder="Ton nom de famille"),
                     MultiWidgetField('birth_date',
                                      attrs=(
                                          {'style': 'width: 30%; display: inline-block; margin-right: 3%;'}), ),
                     css_class="my-3",
                     style="min-height: 46vh;"
                     ),

            Div(StrictButton('<span class="fas fa-chevron-right" ></span> Suivant',
                             type='button',
                             css_class='btn bg-2 btnNext px-3'
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

            Div(StrictButton('Précédent <span class="fas fa-chevron-left" ></span>',
                             type='button',
                             css_class='btn bg-1 btnPrevious px-3'
                             ),

                StrictButton('<span class="fas fa-check" ></span> Valider',
                             type='submit',
                             css_class='btn bg-2 px-3'
                             ),

                css_class="offset-md-4 col-md-8 text-right my-1"
                )

            ),

        css_class="my-5"
    )
)

# =================================
# Layout for LoginForm
# =================================

layout_login = Layout(
    Field('email', placeholder='email@example.com'),
    Field('password', placeholder="Mot de passe..."),
    Div(StrictButton('<span class="fas fa-check" ></span> Se connecter',
                     type='submit',
                     css_class='bg-1 col-md-12 mt-3 px-3'
                     ),
        css_class='offset-md-3 col-md-6'
        )

)
