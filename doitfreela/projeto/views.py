from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import *
from .forms import *
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
  success_url = '/projetos/'



def requisitos(request, pk_projeto):
  requisitos = Requisitos.objects.filter(projeto=pk_projeto)
  return render(request, 'requisito/requisitos_list.html', {'requisitos': requisitos, 'pk_projeto': pk_projeto})

def novo_requisito(request, pk_projeto):
  form = RequisitoForm()
  if request.method == "POST":
    form = RequisitoForm(request.POST)
    if form.is_valid():
        requisito = form.save(commit=False)
        requisito.requisito_id = pk_projeto;
        requisito.save()
        return redirect(reverse('projeto.requisito', args=[pk_projeto]))
  return render(request, 'requisito/requisito_form.html', {'form': form})

def editar_requisito(request, pk_projeto, pk):
    requisito = get_object_or_404(Requisitos, pk=pk)
    form = RequisitoForm(instance=requisito)
    if request.method == "POST":
        form = RequisitoForm(request.POST, instance=requisito)
        if form.is_valid():
            form.save()
            return redirect(reverse('projeto.requisito', args=[pk_projeto]))

    return render(request, 'requisito/requisito_form.html', {'form': form})


def remover_requisito(request, pk_projeto, pk):
    requisito = get_object_or_404(Requisitos, pk=pk)
    requisito.delete()
    return redirect(reverse('projeto.requisito', args=[pk_projeto]))
