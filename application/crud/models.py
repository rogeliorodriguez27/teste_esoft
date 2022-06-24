# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models



class Products(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nome', )
    price = models.PositiveIntegerField( verbose_name='preço' )
    stock = models.PositiveIntegerField( verbose_name='Stock', )
    def __str__(self):
        return "{}: ID: {}, ".format(self.name, self.id,)


        
    class Meta:
        verbose_name = 'produtos'
        ordering = ['id']

