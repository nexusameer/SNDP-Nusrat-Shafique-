from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from django.core.mail import send_mail
from .forms import *
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        context['persona'] = Persona.objects.all()
        context['category'] = Category.objects.all()
        context['services'] = Service.objects.all()
        context['testominals'] = Testimonal.objects.all()
        context['products'] = Product.objects.all()
        
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                email,
                ['ameerh10fw@gmail.com'],
                fail_silently=False,
            )
            form.save()
            return redirect('home')
        else:
            return render(request, 'index.html', {'form': form, 'persona': Persona.objects.all(), 'category': Category.objects.all(), 'services': Service.objects.all(), 'products':Product.objects.all(), 'testominals': Testimonal.objects.all()})


class AboutView(TemplateView):
    template_name = 'about.html'


class ProductView(TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = Product.objects.all()

        return context


class TeamView(TemplateView):
    template_name = 'team.html'