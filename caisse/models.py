from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from datetime import datetime
# Create your models here.
class Caisse(models.Model):
    date=models.DateField(default=datetime.now,blank='true')
    ouverture=models.IntegerField(default=0,blank='true')
    fermeture=models.IntegerField(null=True,blank='true')
    fermeture_prevu=models.IntegerField(default=0,blank='true')

    def __str__(self):
        return str(self.date)


    def save(self, *args, **kwargs):
        try:
            caisse=Caisse.objects.get(id=self.id)
            self.fermeture_prevu+=self.ouverture-caisse.ouverture
            super(Caisse, self).save(*args, **kwargs)
        except ObjectDoesNotExist:
            super(Caisse, self).save(*args, **kwargs)
