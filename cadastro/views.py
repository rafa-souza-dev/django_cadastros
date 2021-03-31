from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


def resultado(request):
    valor_digitado = request.GET.get('resultado', 'This is a default value')
    pessoas = Pessoa.objects.filter(nome=valor_digitado)
    context = {'valor_digitado': valor_digitado,
               'pessoas': pessoas,
               }
    return render(request, 'lista.html', context)
