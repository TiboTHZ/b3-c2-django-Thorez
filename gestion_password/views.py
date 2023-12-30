# gestion_sites/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Site
from .forms import SiteForm

def liste_sites(request):
    sites = Site.objects.filter(user=request.user)
    return render(request, 'gestion_sites/liste_sites.html', {'sites': sites})

def ajouter_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
            return redirect('liste_sites')
    else:
        form = SiteForm()
    return render(request, 'gestion_sites/ajouter_site.html', {'form': form})

def modifier_site(request, pk):
    site = get_object_or_404(Site, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm(instance=site)
    return render(request, 'gestion_sites/modifier_site.html', {'form': form})

def supprimer_site(request, pk):
    site = get_object_or_404(Site, pk=pk, user=request.user)
    site.delete()
    return redirect('liste_sites')
