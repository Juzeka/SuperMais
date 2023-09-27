from django import forms
from django.forms import ModelForm
from dashboard.models import Produto, Categoria


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['categoria','nome','quantidade','valor_pago']

        widgets ={
            'categoria':forms.Select(attrs={'class':'form-control mb-1'}),
            'nome':forms.TextInput(attrs={'class':'form-control mb-1'}),
            'quantidade':forms.NumberInput(attrs={'class':'form-control mb-1','min':'1', 'max':'1000'}),
            'valor_pago': forms.NumberInput(attrs={'class':'form-control mb-1','step':'0.01'})
        }

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nome']

        widgets ={
            'nome':forms.TextInput(attrs={'class':'form-control'}),
        }