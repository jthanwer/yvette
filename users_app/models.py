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
