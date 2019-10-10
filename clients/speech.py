import pyttsx3
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import SeanceHistorique
def speak(client):
    try:
        if(SeanceHistorique.objects.filter(client=client).order_by('-date_heure')[1]):
            last_seance=", dernière présence : "+str(naturaltime(SeanceHistorique.objects.filter(client=client).order_by('-date_heure')[1].date_heure))
        else:
            last_seance=", dernière présence : "+str(naturaltime(SeanceHistorique.objects.filter(client=client).order_by('-date_heure')[0].date_heure))
    except Exception as e:
        print(e)
        last_seance=''
    try:
        if client.seance==0:
            Text ="Bienvenue chez laser straÏke! "+client.nom+" "+client.prenom+". \n "+last_seance+". \n Abonnement  "+client.actif_abonement().forfait.nom+". \n c'est votre derniere partie. Nous vous invitons a renouvler votre abonement."
        else:
            if(client.seance==1):
                Text ="Bienvenue chez laser straÏke! "+client.nom+" "+client.prenom+". \n "+last_seance+". \n Abonnement  "+client.actif_abonement().forfait.nom+". \n Il vous reste une partie."
            else:
                Text ="Bienvenue chez laser straÏke! "+client.nom+" "+client.prenom+". \n "+last_seance+". \n Abonnement  "+client.actif_abonement().forfait.nom+". \n Il vous reste "+str(client.seance)+" parties."

        engine = pyttsx3.init()
        engine.say(Text)
        engine.runAndWait()
    except Exception as e:
        print(e)
    print('yes')


def TextSpeak(Text):
    engine = pyttsx3.init()
    engine.say(Text)
    engine.runAndWait()
