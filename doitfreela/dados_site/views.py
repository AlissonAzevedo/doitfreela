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

  def form_valid(self, form):
      form.instance.usuario = self.request.user
      return super().form_valid(form)

class ProjetoUpdateView(UpdateView):
  model = Projeto
  success_url = '/projetos/'
  

class ProjetoDeleteView(DeleteView):
  model = Projeto
  
