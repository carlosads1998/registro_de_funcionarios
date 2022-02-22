from django.shortcuts import render
from .models import funcionario
from .serializers import funcionarioSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


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