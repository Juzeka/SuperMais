from django import forms
from pedido.models import Pedido, ItemPedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente','endereco']

        widgets = {
            'cliente': forms.TextInput(attrs={'class':'form-control','placeholder':'Cliente'}),
            'endereco': forms.TextInput(attrs={'class':'form-control','placeholder':'Endereço'}),
        }


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido','produto','quantidade']