from django.urls import path

from .views import home
from .views import lista
from .views import pessoa


urlpatterns = [
    path('', home, name='home'),
    path('lista/', lista, name='lista'),
    path('pessoa/<int:pessoa_id>', pessoa, name='pessoa'),
]