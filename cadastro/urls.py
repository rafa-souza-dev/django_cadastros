from django.urls import path

from .views import HomeCreate
from .views import lista
from .views import PessoaUpdate


urlpatterns = [
    path('', HomeCreate.as_view(), name='HomeCreate'),
    path('lista/', lista, name='lista'),
    path('pessoa/<int:pk>', PessoaUpdate.as_view(), name='pessoa'),
]
