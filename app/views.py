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
        context['Service'] = Service.objects.all()
        
        return context