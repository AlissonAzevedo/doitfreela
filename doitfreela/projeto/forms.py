from django.forms import ModelForm
from django import forms
from .models import *

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"
        

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class RequisitoForm(forms.ModelForm):
    class Meta:
        model = Requisitos
        fields = "__all__"