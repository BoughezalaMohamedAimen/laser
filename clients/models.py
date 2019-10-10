from django.db import models
import datetime
from dateutil.relativedelta import relativedelta
from caisse.models import Caisse
from forfaits.models import Forfait
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


# Create your models here.
class Client(models.Model):
    rfid=models.CharField(max_length=255,unique='true')
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    telephone=models.CharField(max_length=10,null='true',blank=True)
    email = models.EmailField(max_length=70,null='true',blank=True)
    seance=models.PositiveIntegerField(default=0)


    def consome(self):
        if self.seance>0:
            self.seance-=1
            SeanceHistorique(client=self).save()
            self.save()

    def __str__(self):
        return self.nom+' '+self.prenom


    def renouvler(self,forfait):
        self.seance+=forfait.nbr_seance
        self.save()


    def actif_abonement(self):
        try:
            return Abonnement.objects.filter(client=self).order_by('-date_heure')[0]
        except:
            return None




class SeanceHistorique(models.Model):
    date_heure=models.DateTimeField(default=datetime.datetime.now, blank='true')
    client=models.ForeignKey(Client,on_delete=models.CASCADE,blank='true',null='true')
    versement=models.PositiveIntegerField(default=0)
    nom=models.CharField(max_length=255,default='Anonnyme')




class Abonnement(models.Model):
    caisse=models.ForeignKey(Caisse,on_delete=models.CASCADE,blank='true')
    date_heure=models.DateTimeField(default=datetime.datetime.now,blank='true')
    forfait=models.ForeignKey(Forfait,on_delete=models.CASCADE,blank='true')
    montant=models.IntegerField(blank='true')
    remise=models.IntegerField(default=0)
    versement=models.IntegerField(default=0)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,blank='true')


from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Abonnement)
def my_handler(sender, **kwargs):
    caisse=Caisse.objects.get(date=datetime.date.today())
    caisse.fermeture_prevu+=kwargs['instance'].versement
    caisse.save()







@receiver(post_delete, sender=Abonnement)
def my_handler_delete(sender, **kwargs):
    caisse=Caisse.objects.get(date=kwargs['instance'].date_heure)
    caisse.fermeture_prevu-=kwargs['instance'].versement
    client=Client.objects.get(id=kwargs['instance'].client.id)
    client.seance-=kwargs['instance'].forfait.nbr_seance
    client.save()
    caisse.save()
