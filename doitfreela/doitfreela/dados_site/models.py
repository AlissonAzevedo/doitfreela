from django.db import models

# Create your models here.
class Projeto(models.Model):
  nome = models.CharField(max_length=250)
  descricao = models.CharField(max_length=250)
  dataCriacao = models.DateTimeField(null=True, auto_now_add=True)
  foto_projeto = models.FileField(upload_to="media/", null=True)

class Usuario(models.Model):
  nome = models.CharField(max_length=250)
  email = models.CharField(max_length=250)
  endereco = models.CharField(max_length=250)
  cidade = models.CharField(max_length=250)
  estado = models.CharField(max_length=250)
  cep = models.IntegerField()
  foto_perfil = models.FileField(upload_to="media/", null=True)

class Ferramenta(models.Model):
  nome = models.CharField(max_length=250)
  descricao = models.CharField(max_length=250)
  foto_ferramenta = models.FileField(upload_to="media/", null=True)
