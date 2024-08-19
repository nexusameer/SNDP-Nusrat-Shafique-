from django.db import models

# Create your models here.

class Persona(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    insta_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    

class Service(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    service_image = models.ImageField()

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    types = models.ManyToManyField(Type)

    def __str__(self):
        return self.name