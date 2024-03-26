from django import forms
from .models import equiposSpare, tecnicoResidente,contratosEquipos


class spareForm(forms.ModelForm):
    class Meta:
        model = equiposSpare
        fields = '__all__' 

class tecnicoForm(forms.ModelForm):
    class Meta:
        model = tecnicoResidente
        fields = '__all__'
        
        
class contratoForm(forms.ModelForm):
    class Meta:
        model = contratosEquipos
        fields = '__all__'
