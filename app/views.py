from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context['persona'] = Persona.objects.all()
        context['category'] = Category.objects.all()
        context['services'] = Service.objects.all()
        context['testominals'] = Testimonal.objects.all()
        context['products'] = Product.objects.all()
        
        return context

class AboutView(TemplateView):
    template_name = 'about.html'


class ProductView(TemplateView):
    template_name = 'products.html'


class TeamView(TemplateView):
    template_name = 'team.html'