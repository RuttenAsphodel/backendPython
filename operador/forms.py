from django import forms
from .models import *


class ubicacionesForm(forms.ModelForm):
    class Meta:
        model = ubicaciones
        fields = '__all__'
        
class especialistasForm(forms.ModelForm):
    class Meta:
        model = especialistas
        fields = '__all__'
        
class proyectosForm(forms.ModelForm):
    class Meta:
        model = proyectos
        fields = '__all__'
        
class solucionesForm(forms.ModelForm):
    class Meta:    
        model = soluciones
        fields = '__all__'

class modeloequipoForm(forms.ModelForm):
    class Meta:
        model = modeloEquipos
        fields = '__all__'
        
class informaticosForm(forms.ModelForm):
    class Meta:
        model = informaticos
        fields = '__all__'
        
class ordenesForm(forms.ModelForm):
    class Meta:
        model = ordenes
        fields = '__all__'
