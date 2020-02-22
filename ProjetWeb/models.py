from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image

class Produit(models.Model):
    numProduit = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=30)
    desciption = models.TextField()
    #images = ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    prixBase = DecimalField(max_digits=6, decimal_places=1)
    dateDebut = models.DateTimeField(default=timezone.now, verbose_name="Date de début de l'enchère")
    dateFin = models.DateTimeField(verbose_name="Date de fin de l'enchère")
    vendeurFK = models.ForeignKey(Vendeur, on_delete=models.CASCADE, db_column='numVendeur')
    categorieFK = models.ForeignKey(Categorie, on_delete=models.CASCADE, db_column='numCategorie')

    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    numVendeur = models.AutoField(primary_key=True)
    nomVendeur = models.CharField(max_length=30)
    prenomVendeur = models.CharField(max_length=30)
    mailVendeur = models.EmailField()
    produits = models.ManyToManyField(Produit, through='Offre', related_name='+')
    noteVendeur = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    

    def __str__(self):
        return self.nomVendeur

"""class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)*/"""


class Acheteur(models.Model):
    numAcheteur = models.AutoField(primary_key=True)
    nomAcheteur = models.CharField(max_length=30)
    prenomAcheteur = models.CharField(max_length=30)
    mailAcheteur = models.EmailField()
    noteAcheteur = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    adresseAcheteur = models.TextField()
    
    

    def __str__(self):
        return self.nomAcheteur


class Categorie(models.Model):
    Categorie_choices = (
        ('Emploi', 'Véhicules'),
        ('Vacances', 'Loisirs'),
        ('Mode', 'Multimédia'),
        ('Maison', 'Autre')
    )
    numCategorie = models.AutoField(primary_key=True)
    libelleCategorie = models.CharField(blank=True, max_length=5, choices=Categorie_choices)

    def __str__(self):
        return self.libelleCategorie


class Enchere(models.Model):
    numEnchere = models.AutoField(primary_key=True)
    montant = models.DecimalField(max_digits=6, decimal_places=1,validators=[MinValueValidator(0.5)])
    commentaire = models.CharField(max_length=50)
    produitFK = models.ForeignKey(Produit, on_delete=models.CASCADE, db_column='numProduit')
    acheteurFK = models.ForeignKey(Acheteur, on_delete=models.CASCADE, db_column='numAcheteur')

    
    def __str__(self):
        return self.nomAcheteur