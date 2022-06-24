# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    cep = models.CharField(verbose_name='CEP',  max_length=9,)
    address = models.CharField(max_length=30, verbose_name='Endereço', )
    number = models.PositiveIntegerField(default=0, verbose_name='Número', validators=[MaxValueValidator(9999)],)
    complement = models.CharField(max_length=20, verbose_name='Complemento', null=True, blank=True )
    neighborhood = models.CharField(max_length=20, verbose_name='Bairro', )
    city = models.CharField(max_length=20, verbose_name='Cidade', )
    uf = models.CharField( max_length=2, verbose_name='Unidade federativa', default='MG')
    email = models.EmailField(_('email address'), unique=True)
    username = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email