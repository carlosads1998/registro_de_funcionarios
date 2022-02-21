from distutils.command.upload import upload
from django.db import models

def upload_image_funcionario(instance, filename):
    return f'{instance.nome}-{filename}'

class funcionario(models.Model):
    nome = models.CharField(max_length=250)
    usuario = models.CharField(max_length=100)
    identificador = models.IntegerField()
    ano = models.IntegerField()
    atualizacao = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_funcionario, blank=True, null = True)