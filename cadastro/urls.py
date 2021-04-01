from django.urls import path

from .views import HomeCreate
from .views import lista
from .views import tabela
from .views import resultado
from .views import PessoaUpdate
from .views import PessoaDelete


urlpatterns = [
    path('', HomeCreate.as_view(), name='HomeCreate'),
    path('lista/', lista, name='lista'),
    path('tabela/', tabela, name='tabela'),
    path('reultado/', resultado, name='resultado'),
    path('pessoa/<int:pk>', PessoaUpdate.as_view(), name='pessoa'),
    path('deletar/<int:pk>', PessoaDelete.as_view(), name='deletar'),
]
