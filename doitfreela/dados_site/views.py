from django.shortcuts import get_object_or_404, render
from django.views.generic import *
from dados_site.forms import *
from .models import *

# Create your views here.

class ListProjetoView(ListView):
  model = Projeto
  queryset = Projeto.objects.all()

class ProjetoCreateView(CreateView):
  model = Projeto
  form_class = ProjetoForm
  success_url = '/projetos/'

class ProjetoUpdateView(UpdateView):
  model = Projeto
  success_url = '/projetos/'
  

class ProjetoDeleteView(DeleteView):
  model = Projeto
  
