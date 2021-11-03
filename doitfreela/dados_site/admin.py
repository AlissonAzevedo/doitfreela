from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
 list_display = ('nome', 'descricao')
 
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
 list_display = ('nome', 'email')
 
@admin.register(Ferramenta)
class FerramentaAdmin(admin.ModelAdmin):
 list_display = ('nome', 'descricao')


