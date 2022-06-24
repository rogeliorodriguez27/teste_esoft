# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Products(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nome', )
    price = models.FloatField(verbose_name='preço', validators=[MinValueValidator(0.0), MaxValueValidator(99999999.0)])
    stock = models.PositiveIntegerField( verbose_name='Stock', validators=[MaxValueValidator(9999)],)
    def __str__(self):
        return "{}: ID: {}, ".format(self.name, self.id,)


        
    class Meta:
        verbose_name = 'produtos'
        ordering = ['name', '-price', '-stock']

