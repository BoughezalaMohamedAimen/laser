from django import forms
from .models import *
import datetime
class ClientForm(forms.ModelForm):
    prefix = 'add'
    class Meta:
            model=Client
            fields='__all__'

class UpdateClientForm(forms.ModelForm):
    prefix = 'update'
    class Meta:
            model=Client
            fields='__all__'

class AbonnementForm(forms.ModelForm):
    prefix='abonnement'
    class Meta:
        model=Abonnement
        fields='__all__'
