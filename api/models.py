from distutils.command.upload import upload
from email.mime import base
from lib2to3.pytree import Base
from random import choice
from django.db import models

def upload_image_funcionario(instance, filename):
    return f'{instance.nome}-{filename}'


class Base(models.Model):
    funcionario=models.DateTimeField(auto_now_add=True)
    class Meta:
         abstract = True
                                             

class funcionario(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'empregado'),
        ('desativado', 'demitido'),
    )
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('N', 'Prefiro não informar'),
    )
    
    
    sexo= models.CharField(max_length = 20, choices=SEXO_CHOICES, default=1)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default=1)
    nome = models.CharField(max_length=250)
    usuario = models.CharField(max_length=100, unique=True)
    identificador = models.IntegerField(unique=True)
    ano = models.IntegerField()
    atualizacao = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_funcionario, blank=True, null = True)
