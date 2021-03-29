from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    idade = models.PositiveIntegerField(max_length=3)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=40)
    apelido = models.CharField(max_length=20, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.nome


    class Meta:
        ordering = ['nome', 'sobrenome']
