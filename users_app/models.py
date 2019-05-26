from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
import datetime as dt

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Adresse email', unique=True)
    first_name = models.CharField(verbose_name='Prénom', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Nom', max_length=30, blank=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    birth_date = models.DateField(verbose_name='Date de naissance')
    date_joined = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)
    city = models.CharField(max_length=50, verbose_name='Ville')
    photo = models.ImageField(verbose_name='Photo de profil', blank=True, null=True)
    coloc = models.ForeignKey('mainapp.Colocation', related_name='tenants', on_delete=models.SET_NULL,
                              blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def age(self):
        """
        Compute the age for the User.
        """
        born = self.birth_date
        today = dt.date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


