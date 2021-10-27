from django.shortcuts import get_object_or_404, render
from .models import Projeto
from .models import Usuario

# Create your views here.

def home(request):
   
  projeto = Projeto.objects.all()
  usuario = Usuario.objects.all()

  dados = {
    'projeto': projeto,
    'usuario': usuario[0],
  }

  return render(request, "home.html", dados)

#Create your views here.
def perfil(request):

  usuario = Usuario.objects.all()

  dadosUser = {
    'usuario': usuario[0],
  }
  return render(request, "perfil.html", dadosUser)

def projeto(request, id):

  projeto = get_object_or_404(Projeto, pk=id)
  
  dadosProjeto = {
    'projeto': projeto,
  }
  return render(request, "projeto.html", dadosProjeto)


def gestao_de_tempo(request):

  return render(request, "gestao_tempo.html")

