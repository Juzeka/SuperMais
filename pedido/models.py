from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from core import settings
from dashboard.models import Produto


class Pedido(models.Model):
    cliente = models.CharField(max_length=100, blank=False,verbose_name='Cliente')
    endereco = models.CharField(max_length=100, blank=False,verbose_name='Endereço')
    pago = models.BooleanField(auto_created=True, default=True, verbose_name='Pago')

    def get_total_pedido(self):
        return sum(pedido.get_total_preco() for pedido in self.pedidos.all())


    def __str__(self):
        return str(f'Pedido {self.id}')


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido,related_name='pedidos',on_delete=models.CASCADE, verbose_name='Pedido')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(int(settings.CARRINHO_SESSION_ID)),])


    def get_total_preco(self):
        return self.preco * self.quantidade


    def __str__(self):
        return str(self.id)