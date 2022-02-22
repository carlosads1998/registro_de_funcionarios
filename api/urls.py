from django.urls import path
from .views import funcionarioApiView, funcionariosApiView

urlpatterns = [
    path('funcionario/', funcionarioApiView.as_view(), name = 'funcionario'),
    path('funcionario/<int:pk>/', funcionariosApiView.as_view(), name = 'funcionaros'),
    
]
