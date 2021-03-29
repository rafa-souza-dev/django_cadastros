from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Pessoa


def home(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'home.html', {'pessoas': pessoas})


def lista(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'lista.html', {'pessoas': pessoas})


def pessoa(request, pessoa_id):
    pessoas = Pessoa.objects.all()
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)

    return render(request, 'pessoa.html', {'pessoas': pessoas,
                                           'pessoa': pessoa})
