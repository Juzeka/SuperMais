import decimal

from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='Categoria')

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    nome = models.CharField(max_length=150, unique=True, blank=False, null=False, verbose_name='Produto')
    quantidade = models.IntegerField(blank=False, null=False, verbose_name='Quantidade')
    valor_pago = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False,verbose_name='Valor Pago')
    preco_medio = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False,verbose_name='Preço Atacado')
    data_criada = models.DateTimeField(auto_now_add=True, verbose_name='Criado')
    data_modificacao = models.DateTimeField(auto_now=True,verbose_name='Modificado')
    status = models.BooleanField(default=True, auto_created=True)

    def __str__(self):
        return self.nome