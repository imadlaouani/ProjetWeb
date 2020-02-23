from django.shortcuts import render
from django.http import HttpResponse, Http404 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage
from .forms import *

def home(request):
    return render(request, 'home.html')


def inscription(request):
    error = False

    if request.method == "POST":
        form = AcheteurForm(request.POST)
        form.save()
        if form.is_valid():
            #On inscrit l'acheteur
            acheteur = Acheteur(nomAcheteur=form.cleaned_data['last_name'], prenomAcheteur=form.cleaned_data['first_name'],mailAcheteur = form.cleaned_data['email'],adresseAcheteur = form.cleaned_data['adresseAcheteur'])
            acheteur.save()
            # On le connecte
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            login(request, authenticate(username=username, password=password))  # nous connectons l'utilisateur
            
    else:
        form = AcheteurForm()

    return render(request, 'inscription.html', locals())



def inscription_vendeur(request):
    if request.method == 'POST':
        form = VendeurForm(request.POST)
        
        if form.is_valid():
            form.save() #Sauvegarde/Creation d'un utilisateur de base
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #Authentification de l'utilisateur
          # On ajoute l'utilisateur au groupe étudiant ici (id groupe étudiant = 2 )
            Vendeur = Vendeur(username = User.objects.get(username=username),nomVendeur=form.cleaned_data[last_name], prenomVendeur=form.cleaned_data[first_name],mailVendeur=form.cleaned_data.get('email'))
            Vendeur.save()  # Sauvegarde de l'étudiant
            login(request, user) #Connexion au site
            return redirect('')
    else:
        form = VendeurForm(request.POST)
    return render(request, 'inscription.html', {'form': form})