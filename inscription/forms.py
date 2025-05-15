from django import forms
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'  # or specify the fields you want to include
