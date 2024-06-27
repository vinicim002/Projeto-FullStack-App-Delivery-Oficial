from django.contrib import admin
from .models import ItemMenu

@admin.register(ItemMenu)
class ItemMenuAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'disponivel', 'categoria', 'data_adicionado', 'ultima_atualizacao')
    list_filter = ('disponivel', 'categoria', 'data_adicionado')
    search_fields = ('nome', 'descricao')
