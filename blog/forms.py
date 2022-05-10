from django import forms
from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']
        # le champ "upload" est géré dans view.py
        # le champ "date_upload" se met à la date du jour automatiquement





