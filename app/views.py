from django.shortcuts import render, redirect, get_object_or_404
from .models import Site, SiteForm, SiteUpdateForm

def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'sites/liste_sites.html', {'sites': sites})

def ajout_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm()

    return render(request, 'sites/add_sites.html', {'form': form})

def modifier_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        form = SiteUpdateForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteUpdateForm(instance=site)

    return render(request, 'sites/modifier_site.html', {'form': form, 'site': site})

def supprimer_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    site.delete()
    return redirect('liste_sites')
