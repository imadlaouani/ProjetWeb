from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class Vendeur(models.Model):
    numVendeur = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    nomVendeur = models.CharField(max_length=30)
    prenomVendeur = models.CharField(max_length=30)
    mailVendeur = models.EmailField()
    noteVendeur = models.IntegerField(blank=True,validators=[MinValueValidator(0), MaxValueValidator(5)])
    class Meta:
        db_table ='vendeur'

    def __str__(self):
        return self.nomVendeur





class Acheteur(models.Model):
    
    numAcheteur = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    nomAcheteur = models.CharField(max_length=30)
    prenomAcheteur = models.CharField(max_length=30)
    mailAcheteur = models.EmailField()
    noteAcheteur = models.IntegerField(blank = False,validators=[MinValueValidator(0), MaxValueValidator(5)])
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
    libelleCategorie = models.CharField(blank=True, max_length=30, choices=Categorie_choices)

    class Meta:
        db_table = 'categorie'

    def __str__(self):
        return self.libelleCategorie

class Produit(models.Model):
    numProduit = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=30)
    desciption = models.TextField()
    images = models.    ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    prixBase =  models.FloatField(validators=[MinValueValidator(0)])
    dateDebut = models.DateTimeField(default=timezone.now, verbose_name="Date de début de l'enchère")
    dateFin = models.DateTimeField(verbose_name="Date de fin de l'enchère")
    vendeurFK = models.ForeignKey(Vendeur, on_delete=models.CASCADE, db_column='numVendeur')
    categorieFK = models.ForeignKey(Categorie, on_delete=models.CASCADE, db_column='numCategorie')

    def __str__(self):
        return self.nom


class Enchere(models.Model):
    numEnchere = models.AutoField(primary_key=True)
    montant = models.DecimalField(max_digits=6, decimal_places=1,validators=[MinValueValidator(0.5)])
    commentaire = models.CharField(max_length=50)
    produitFK = models.ForeignKey(Produit, on_delete=models.CASCADE, db_column='numProduit')
    acheteurFK = models.ForeignKey(Acheteur, on_delete=models.CASCADE, db_column='numAcheteur')

    
    def __str__(self):
        return self.nomAcheteur