# myapp/views.py
from django.shortcuts import render, redirect
from .models import Site, SiteForm

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
