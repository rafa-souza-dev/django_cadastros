from cadastro import requisicao

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

resposta = requisicao.requisicao('https://gerador-nomes.herokuapp.com/nome/aleatorio')
nome = requisicao.parsing(resposta)


def nome_aleatorio():
    return nome[0]


def sobrenome_aleatorio():
    return nome[1]


class Pessoa(models.Model):
    nome = models.CharField(max_length=20, default=nome_aleatorio)
    sobrenome = models.CharField(max_length=15, default=sobrenome_aleatorio)
    idade = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)],
                                        verbose_name='Idade')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', help_text='exemplo: 22/06/2002')
    email = models.EmailField(max_length=32, verbose_name='E-mail', help_text='exemplo@contato.com', unique=True)
    apelido = models.CharField(max_length=20, null=True, blank=True)
    observacao = models.CharField(max_length=32, null=True, blank=True, verbose_name='Observação')


    def __str__(self):
        return self.nome


    class Meta:
        ordering = ['nome', 'sobrenome']
