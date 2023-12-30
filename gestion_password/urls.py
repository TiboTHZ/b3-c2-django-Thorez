from django.urls import path
from .views import liste_sites, ajouter_site, modifier_site, supprimer_site

urlpatterns = [
    path('', liste_sites, name='liste_sites'),
    path('ajouter/', ajouter_site, name='ajouter_site'),
    path('modifier/<int:pk>/', modifier_site, name='modifier_site'),
    path('supprimer/<int:pk>/', supprimer_site, name='supprimer_site'),
]
