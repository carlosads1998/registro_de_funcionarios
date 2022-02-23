from distutils.command.upload import upload
from email.mime import base
from lib2to3.pytree import Base
from django.db import models

def upload_image_funcionario(instance, filename):
    return f'{instance.nome}-{filename}'


class Base(models.Model):
    funcionario=models.DateTimeField(auto_now_add=True)
    class Meta:
         abstract = True
                                             

class funcionario(models.Model):
    
    nome = models.CharField(max_length=250)
    usuario = models.CharField(max_length=100, unique=True)
    identificador = models.IntegerField(unique=True)
    ano = models.IntegerField()
    atualizacao = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_funcionario, blank=True, null = True)
