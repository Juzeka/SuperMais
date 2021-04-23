from django.db import models
from dashboard.models import Produto


class Compra(models.Model):
    cliente = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente