# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView

# Create your views here.



class indexView(TemplateView):

    template_name = "index.html"
