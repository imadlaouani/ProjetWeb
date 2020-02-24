from django.shortcuts import render
from django.http import HttpResponse, Http404 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage
from .forms import *
from django.contrib.auth.forms import AuthenticationForm

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


