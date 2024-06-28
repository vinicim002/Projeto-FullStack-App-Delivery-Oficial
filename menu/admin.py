from django.contrib import admin
from .models import Categoria, ItemMenu


@admin.register(ItemMenu)
class ItemMenuAdmin(admin.ModelAdmin):
    list_display = ('icone', 'preco', 'nome_produto', 'categoria', 'data_adicionado', 'ultima_atualizacao', 'disponivel')
    list_filter = ('disponivel', 'categoria', 'data_adicionado')
    search_fields = ('preco', 'disponivel')

admin.site.register(Categoria)  # Registro da Categoria


