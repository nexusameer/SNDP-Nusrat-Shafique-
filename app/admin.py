from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.register([Persona, Category, Service, Type, Product, Testimonal, Contact])