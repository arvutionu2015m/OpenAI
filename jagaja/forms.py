from django import forms
from .models import Ülesanne

class ÜlesanneVorm(forms.ModelForm):
    class Meta:
        model = Ülesanne
        fields = ['pealkiri', 'kirjeldus', 'pilt', 'tähtaeg']
        widgets = {
            'tähtaeg': forms.DateInput(attrs={'type': 'date'}),
        }