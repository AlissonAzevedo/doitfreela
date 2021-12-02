from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', login_required(ListProjetoView.as_view()), name='projeto.index'),
    path('novo/', login_required(ProjetoCreateView.as_view()), name='projeto.novo'),
    path('<int:pk>/editar', login_required(ProjetoUpdateView.as_view()), name='projeto.editar'),
    path('<int:pk>/remover', login_required(ProjetoDeleteView.as_view()), name='projeto.remover'),
    path('<int:pk_projeto>/requisito', login_required(views.requisitos), name='projeto.requisito'),
    path('<int:pk_projeto>/requisito/novo/', login_required(views.novo_requisito), name='requisito.novo'),
    path('<int:pk_projeto>/requisito/<int:pk>/editar', login_required(views.editar_requisito), name='requisito.editar'),
    path('<int:pk_projeto>/requisito/<int:pk>/remover', login_required(views.remover_requisito), name='requisito.remover'),
] 
if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)