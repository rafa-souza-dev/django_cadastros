from django.urls import path

from .views import home
from .views import lista


urlpatterns = [
    path('', home, name='home'),
    path('lista/', lista, name='lista'),
]