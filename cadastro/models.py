from cadastro import requisicao

from django.db import models


resposta = requisicao.requisicao('https://gerador-nomes.herokuapp.com/nome/aleatorio')
nome = requisicao.parsing(resposta)


def nome_aleatorio():
    return nome[0]


def sobrenome_aleatorio():
    return nome[1]


class Pessoa(models.Model):
    nome = models.CharField(max_length=20, default=nome_aleatorio)
    sobrenome = models.CharField(max_length=15, default=sobrenome_aleatorio)
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    email = models.CharField(max_length=40)
    apelido = models.CharField(max_length=20, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.nome


    class Meta:
        ordering = ['nome', 'sobrenome']
