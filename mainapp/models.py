from django.db import models
from users_app.models import Profile
from django.contrib import messages


class Colocation(models.Model):
    owner = models.OneToOneField('users_app.Profile', on_delete=models.CASCADE, related_name='owner')
    intro = models.TextField('Une petite description')
    two_words = models.CharField('Votre coloc en deux mots', max_length=40)
    mean_age = models.IntegerField(null=True)
    pets = models.CharField('Animaux présents dans la coloc', max_length=40)

    class Meta:
        verbose_name = 'Colocation'
        ordering = ['intro']

    @classmethod
    def add_tenant(cls, request, id_coloc, user_profile):
        coloc = cls.objects.get(id=id_coloc)
        if coloc.owner == user_profile:
            messages.add_message(request, messages.WARNING, 'Impossible d\'intégrer une coloc quand vous en '
                                                            'êtes déjà le créateur !')
        elif coloc.owner == user_profile:
            messages.add_message(request, messages.WARNING, 'Impossible d\'intégrer une coloc quand vous '
                                                            'êtes déjà le créateur de l\'une d\'elles !')
        elif user_profile.coloc:
            messages.add_message(request, messages.WARNING, 'Impossible d\'intégrer une coloc quand vous '
                                                            'êtes déjà dans l\'une d\'elles !')
        else:
            user_profile.coloc = coloc
            user_profile.save()
            cls.update_mean_age(id_coloc)

    @classmethod
    def remove_tenant(cls, request, id_coloc, user_profile):
        user_profile.coloc = None
        user_profile.save()
        cls.update_mean_age(id_coloc)

    @classmethod
    def update_mean_age(cls, id_coloc):
        coloc = cls.objects.get(id=id_coloc)
        tenants = coloc.tenants.all()
        coloc.mean_age = (coloc.owner.age + sum([tenant.age for tenant in tenants])) / (1 + len(tenants))
        coloc.save()

