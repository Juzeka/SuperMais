from django import forms
from pedido.models import Pedido, ItemPedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente','endereco']


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido','produto','quantidade']