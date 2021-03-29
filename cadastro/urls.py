from django.urls import path

from .views import HomeCreate
from .views import lista
from .views import pessoa


urlpatterns = [
    path('', HomeCreate.as_view(), name='HomeCreate'),
    path('lista/', lista, name='lista'),
    path('pessoa/<int:pessoa_id>', pessoa, name='pessoa'),
]