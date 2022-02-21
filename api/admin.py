from django.contrib import admin
from .models import funcionario

@admin.register(funcionario)
class funcionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'identificador', 'ano', 'image', 'atualizacao')
