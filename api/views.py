from .models import funcionario
from .serializers import funcionarioSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class funcionarioApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['usuario']

class funcionariosApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['usuario']