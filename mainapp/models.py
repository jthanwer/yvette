from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField('Ville', max_length=20)

    class Meta:
        verbose_name = "Profil"
        ordering = ['age']

    def __str__(self):
        return "{} {} ({} ans)".format(self.user.first_name, self.user.last_name, self.age)


class Colocation(models.Model):
    createur = models.OneToOneField(Profil, on_delete=models.CASCADE)
    intro = models.TextField('Une petite description')
    two_words = models.CharField('Votre coloc en deux mots', max_length=40)
    mean_age = models.IntegerField(null=True)
    pets = models.CharField('Animaux présents dans la coloc', max_length=40)

    class Meta:
        verbose_name = 'Colocation'
        ordering = ['intro']

