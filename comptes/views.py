
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage
from ProjetWeb.forms import *
from ProjetWeb.models import *
# Create your views here.

"""def inscription(request):
	if request.method == 'POST':
		form = VendeurForm(request.POST)
		if form.is_valid():
			form.save()
			# On crée un vendeur
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
            Utilisateur = User.objects.get(username = username)
            vendeur = Vendeur(numVendeur = Utilisateur,nomVendeur = form.cleaned_data.get('last_name') ,prenomVendeur = form.cleaned_data.get('first_name'), mailVendeur=form.cleaned_data.get('email'))
            vendeur.save()  
			login(request,user)# On le connecte
			return redirect('home')
	else:
		form = VendeurForm()
		return render(request,'comptes/inscription.html',{'form':form})"""
groupe_prof = Group(id='1',name='professeur')
groupe_prof.save()
groupeVendeur = Group(id='2',name='Vendeur')
groupeVendeur.save()

def inscription(request):
    if request.method == 'POST':
        form = VendeurForm(request.POST)
        if form.is_valid():
            form.save() #Sauvegarde/Creation d'un utilisateur de base
            username = form.cleaned_data.get('username')
            mail = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
             #Authentification de l'utilisateur
            Utilisateur = User.objects.create_user(username=username,email=mail,password=raw_password)
            user = authenticate(username=username, password=raw_password)
            #User.objects.create_user('Maxime', 'maxime@crepes-bretonnes.com', 'm0nsup3rm0td3p4ss3')
            vendeur = Vendeur(numVendeur=Utilisateur,nomVendeur=form.cleaned_data.get('last_name'),prenomVendeur=form.cleaned_data.get('first_name'), mailVendeur=form.cleaned_data.get('email'))
            groupeVendeur = Group.objects.get(id='2')  # On ajoute l'utilisateur au groupe Vendeur ici (id groupe étudiant = 2 )
            vendeur.save()
            login(request, user) #Connexion au site
            estVendeur = True
            request.session[estVendeur] = estVendeur # Sauvegarde de l'étudiant # On mémorise le fait que c'est un étudiant en session
            return redirect('home')
    else:
        form = VendeurForm(request.POST)
    return render(request,'comptes/inscription.html',{'form':form})



def connexion(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# On récupère et connecte l'utilisateur
			user=form.get_user()
			login(request,user)
			return redirect('home')

	else:
		form = AuthenticationForm()
		return render(request,'comptes/connexion.html',{'form':form})

def logout_user(request):
    logout(request)
    return render(request, 'home.html')