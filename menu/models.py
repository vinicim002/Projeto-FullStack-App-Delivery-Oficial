from django.db import models

class ItemMenu(models.Model):
    CATEGORIA_CHOICES = [
        ('menu_principal', 'Menu Principal'),
        ('almoco', 'Almoço'),
        ('vegetariano', 'Vegetariano'),
        ('sobremesa', 'Sobremesa'),
        ('pizza', 'Pizza'),
        ('infantil', 'Infantil'),
        ('bebida_nao_alcoolica', 'Bebida Não Alcoólica'),
        ('bebida_alcoolica', 'Bebida Alcoólica'),
        ('vinho', 'Vinho'),
    ]

    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    data_adicionado = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='menu/', blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    class Meta:
        verbose_name = "Item Menu"
