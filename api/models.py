from django.db import models

class funcionario(models.Model):
    nome = models.CharField(max_length=250)
    usuario = models.CharField(max_length=100)
    identificador = models.IntegerField()
    ano = models.IntegerField()
    atualizacao = models.DateField(auto_now_add=True)
    