"""doitfreela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dados_site.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('perfil', perfil, name='perfil'),
    path('projeto/<int:pk>/', projeto, name='projeto'),
    path('projeto/ferramentas/<int:pk>/', ferramentas, name= 'ferramentas'),
    path('gestao_de_tempo', gestao_de_tempo, name= 'gestao_de_tempo'),
    path('projeto/ferramentas/requisitos', requisitos, name= 'requisitos'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)