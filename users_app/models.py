from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField('Ville', max_length=20)
    photo = models.ImageField(null=True)
    coloc = models.ForeignKey('mainapp.Colocation', related_name='tenants', on_delete=models.SET_NULL,
                              null=True)

    class Meta:
        verbose_name = "Profile"
        ordering = ['age']

    def __str__(self):
        return "{} {} ({} ans)".format(self.user.first_name, self.user.last_name, self.age)
