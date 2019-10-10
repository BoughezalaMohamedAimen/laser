from django import forms
from .models import *


class ForfaitForm(forms.ModelForm):
    prefix = 'add'
    class Meta:
            model=Forfait
            fields='__all__'

class UpdateForfaitForm(forms.ModelForm):
    prefix = 'update'
    class Meta:
            model=Forfait
            fields='__all__'
