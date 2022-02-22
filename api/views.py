from django.shortcuts import render
from .models import funcionario
from .serializers import funcionarioSerializer
from rest_framework import generics

class funcionarioApiView(generics.ListCreateAPIView):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['usuario']


class funcionariosApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['usuario']
