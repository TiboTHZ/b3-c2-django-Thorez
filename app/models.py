from django import forms
from django.db import models

class Site(models.Model):
    nom = models.CharField(max_length=100)
    url = models.URLField()
    identifiant = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['nom', 'url', 'identifiant', 'mot_de_passe']

class SiteUpdateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['nom', 'url', 'identifiant', 'mot_de_passe']