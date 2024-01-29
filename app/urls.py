from django.urls import path
from .views import liste_sites, ajout_site

urlpatterns = [
    path('', liste_sites, name='accueil'),
    path('liste-sites/', liste_sites, name='liste_sites'),
    path('ajout-site/', ajout_site, name='ajout_site'),
]