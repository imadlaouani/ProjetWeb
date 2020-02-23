from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ProjetWeb.models import *
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



# Formulaire d'inscription ou de modification d'un acheteur
class AcheteurForm(UserCreationForm):
    adresseAcheteur = forms.CharField(max_length=254)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1', 'password2' )

# Formulaire d'inscription ou de modification d'un vendeur
class VendeurForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1', 'password2' )

# Formulaire de création ou de modification d'un produit
class ProduitForm(forms.Form):
    Categorie_choices = (
        ('Emploi', 'Véhicules'),
        ('Vacances', 'Loisirs'),
        ('Mode', 'Multimédia'),
        ('Maison', 'Autre')
    )
    titre = forms.CharField(max_length=30)
    desciption = forms.CharField(max_length=254)
    images = forms.ImageField(max_length=100)
    prixBase =  forms.FloatField(validators=[MinValueValidator(0)])
    dateDebut = forms.DateTimeField(label="Date de début de l'enchère")
    dateFin = forms.DateTimeField()
    categorie = forms.ChoiceField(label="Catégorie",choices=Categorie_choices)

# Formulaire de création d'une enchère
class EnchereForm(forms.Form):
    montant = forms.DecimalField(max_digits=6, decimal_places=1,validators=[MinValueValidator(0.5)])
    commentaire = forms.CharField(max_length=50)