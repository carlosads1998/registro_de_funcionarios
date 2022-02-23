from multiprocessing import context
from django.shortcuts import render
from .models import funcionario
from .serializers import funcionarioSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from rest_framework_simplejwt.views import TokenObtainPairView


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
    
#class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#    @classmethod
#    def get_token(cls, user):
#        token = super().get_token(user)
#
#        # Add custom claims
#        token['name'] = user.name
#        # ...
#
#        return token
#
#class MyTokenObtainPairView(TokenObtainPairView):
#    serializer_class = MyTokenObtainPairSerializer