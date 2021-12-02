from django.forms import ModelForm
from django import forms
from .models import *

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'custom-select mr-sm-4'}),
        }
        

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class RequisitoForm(forms.ModelForm):
    class Meta:
        model = Requisitos
        fields = "__all__"

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'projeto': forms.Select(attrs={'class':'custom-select mr-sm-4'}),
        }