from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Projeto(models.Model):
  nome = models.CharField(max_length=250)
  descricao = models.CharField(max_length=250)
  dataCriacao = models.DateTimeField(null=True, auto_now_add=True, editable=False)
  #foto_projeto = models.FileField(upload_to="media/", null=True)
  #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.nome

class Usuario(models.Model):
  nome = models.CharField(max_length=250)
  email = models.CharField(max_length=250)
  endereco = models.CharField(max_length=250)
  cidade = models.CharField(max_length=250)
  estado = models.CharField(max_length=250)
  cep = models.IntegerField()
  #foto_perfil = models.FileField(upload_to="media/", null=True)
  usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.nome


class Requisitos(models.Model):
  nome = models.CharField(max_length=250, null=True)
  descricao = models.CharField(max_length=250, null=True)
  dataCriacao = models.DateTimeField('Data de criação', auto_now_add=True, null= True)
  dataAtualizacao = models.DateTimeField('Última data de atualização', auto_now=True, null= True)
  projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.nome

class Documentacao(models.Model):
  nome = models.CharField(max_length=250, null=True)
  arquivo = models.FileField(upload_to="media/", null=True)
  projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.nome

class Tempo(models.Model):
  horaEsperada = models.IntegerField('Horas Esperadas', null= True)
  horaExecutada = models.IntegerField('Horas Executadas', null= True)
  projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True)
