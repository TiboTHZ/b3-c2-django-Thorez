from django.urls import path
from .views import liste_sites, ajout_site, modifier_site, supprimer_site

urlpatterns = [
    path('', liste_sites, name='accueil'),
    path('liste-sites/', liste_sites, name='liste_sites'),
    path('ajout-site/', ajout_site, name='ajout_site'),
    path('modifier-site/<int:site_id>/', modifier_site, name='modifier_site'),
    path('supprimer-site/<int:site_id>/', supprimer_site, name='supprimer_site'),
]