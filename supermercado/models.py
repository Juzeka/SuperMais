from django.db import models
from dashboard.models import Produto


class Compra(models.Model):
    cliente = models.CharField(max_length=50, verbose_name='Cliente')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE,verbose_name='Produto')

    def __str__(self):
        return self.cliente