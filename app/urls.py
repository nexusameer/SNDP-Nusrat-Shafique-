from django.urls import path
from app.views import *

urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('team/', TeamView.as_view(), name='team'),
    path('products/', ProductView.as_view(), name='products'),
]