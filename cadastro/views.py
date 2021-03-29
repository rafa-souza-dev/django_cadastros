from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Pessoa


class HomeCreate(CreateView):
    model = Pessoa
    fields = ['nome', 'sobrenome', 'idade', 'data_nascimento', 'email', 'apelido', 'observacao']
    template_name = 'home.html'
    success_url = reverse_lazy('lista')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome', 'sobrenome', 'idade', 'data_nascimento', 'email', 'apelido', 'observacao']
    template_name = 'pessoa.html'
    success_url = reverse_lazy('lista')


def lista(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'lista.html', {'pessoas': pessoas})
