from django.shortcuts import render

# Create your views here.
from ProjetWeb.forms import ProduitForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from ProjetWeb.models import *

def ajouter_annonce(request):
    """if !(request.session['estEtu']):
        return render(request, 'error404.html')
    else:"""
    if request.method == 'POST':
        utilisateur = User.objects.get(id=request.user.id)
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = Produit(numVendeur = utilisateur,titre=form.cleaned_data["titre"],description = form.cleaned_data["description"],images = form.cleaned_data["images"],prixBase = form.cleaned_data["prixBase"],dateDebut = form.cleaned_data["dateDebut"],dateFin=form.cleaned_data["dateFin"],vendeurFK=request.user.id,categorieFK = form.cleaned_data["categorieFK"])
            produit.save()
            return redirect('home')
            #lire_annonce(request,sub.numSujet)
    else:
        form = ProduitForm()
    return render(request, 'annonces/ajouter.html', locals())
