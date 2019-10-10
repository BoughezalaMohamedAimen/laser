from django import forms
from .models import *


class UpdateCaisseForm(forms.ModelForm):
    prefix = 'update'
    class Meta:
            model=Caisse
            fields='__all__'
