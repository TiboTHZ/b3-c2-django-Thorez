from django.urls import path
from .views import liste_sites

urlpatterns = [
    path('', liste_sites, name='accueil'),
    path('liste-sites/', liste_sites, name='liste_sites'),
]