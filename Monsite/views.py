from django.shortcuts import render
from django.http import HttpResponse, Http404 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage


def inscription_acheteur(request):
    error = False

    if request.method == "POST":
        form = AcheteurForm(request.POST)
        if form.is_valid():
            # Nous inscrivons l'acheteur si les données sont correctes
            acheteur = Acheteur(nomAcheteur=form.cleaned_data['last_name'],PrenomAcheteur=form.cleaned_data['first_name'], mailAcheteur=form.cleaned_data['email'], adresseAcheteur=form.cleaned_data['adresseAcheteur'])
            login(request, authenticate(username=username, password=password))  # nous connectons l'acheteur
            
    else:
        form = ConnexionForm() #Sinon on attend le formulaire

    return render(request, 'inscription.html', locals())

def home(request):
    return render(request, 'home.html')


