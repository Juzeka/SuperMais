from django import forms
from pedido.models import Pedido, ItemPedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente','endereco']

        widgets = {
            'cliente': forms.HiddenInput(attrs={'class':'form-control','value':'Cliente'}),
            'endereco': forms.TextInput(attrs={'class':'form-control','placeholder':'Endereço'}),
        }


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido','produto','quantidade']

        widgets ={
            'pedido': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'type':'number','min':'1'}),
        }