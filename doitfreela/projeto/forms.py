from django.forms import ModelForm
from django import forms
from .models import *

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),

        }
        


class RequisitoForm(forms.ModelForm):
    class Meta:
        model = Requisitos
        fields = "__all__"

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'projeto': forms.Select(attrs={'class':'custom-select mr-sm-4'}),
        }