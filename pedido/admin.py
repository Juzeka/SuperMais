from django.contrib import admin

# Register your models here.
from pedido.models import ItemPedido, Pedido

admin.site.register(ItemPedido)
admin.site.register(Pedido)
