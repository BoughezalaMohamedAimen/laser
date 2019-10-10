from django.db import models

# Create your models here.
class Forfait(models.Model):
    nom=models.CharField(max_length=255)
    nbr_seance=models.PositiveIntegerField()
    prix=models.PositiveIntegerField()

    def __str__(self):
        return self.nom+'  '+str(self.nbr_seance)+' séance '+str(self.prix)+' Dinar'
