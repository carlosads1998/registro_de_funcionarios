from rest_framework import serializers
from .models import funcionario

class funcionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = funcionario
        fields =(
                'id',
                'nome',
                 'usuario',
                 'identificador',
                 'ano',
                 'atualizacao',
                 'image',
       )
