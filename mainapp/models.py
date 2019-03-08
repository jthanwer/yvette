from django.db import models
from django.contrib.auth.models import User
from users_app.models import Profil


class Colocation(models.Model):
    createur = models.OneToOneField(Profil, on_delete=models.CASCADE)
    intro = models.TextField('Une petite description')
    two_words = models.CharField('Votre coloc en deux mots', max_length=40)
    mean_age = models.IntegerField(null=True)
    pets = models.CharField('Animaux présents dans la coloc', max_length=40)

    class Meta:
        verbose_name = 'Colocation'
        ordering = ['intro']

