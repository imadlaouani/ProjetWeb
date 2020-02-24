from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from ProjetWeb.forms import VendeurForm,AcheteurForm
# Create your views here.

def inscription(request):
	if request.method == 'POST':
		form = VendeurForm(data=request.POST)
		if form.is_valid():
			form.save()
			#On connecte l'utilisateur
			user=form.get_user()
			login(request,user)
			return redirect('home')
	else:
		form = UserCreationForm()
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