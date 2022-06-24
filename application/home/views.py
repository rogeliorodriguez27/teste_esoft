# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from crud.models import Products

# Create your views here.
   

class HomeView(TemplateView, LoginRequiredMixin):

    template_name = "home.html"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the products
        context['productsCount'] = Products.objects.all().count()
        return context


