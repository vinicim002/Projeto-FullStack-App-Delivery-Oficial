from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome' ,'email', 'password')
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')

