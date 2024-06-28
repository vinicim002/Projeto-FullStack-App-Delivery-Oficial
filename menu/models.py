from django.db import models
from django.utils.safestring import mark_safe

class Categoria(models.Model):
    categoria = models.CharField(max_length=200)
    
    def __str__(self):
        return self.categoria

class ItemMenu(models.Model):

    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    preco = models.FloatField()
    disponivel = models.BooleanField(default=True)
    data_adicionado = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='post_img', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ingredientes = models.CharField(max_length=200, default="Desconhecido")  # Definindo o valor padrão aqui

    @mark_safe
    def icone(self):
        if self.imagem:
            return f'<img width="30px" src="/media/{self.imagem}">'

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = "Item Menu"
        verbose_name_plural = "Itens do Menu"
