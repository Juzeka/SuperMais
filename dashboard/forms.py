from django import forms
from django.forms import ModelForm
from dashboard.models import Produto, Categoria


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['categoria','nome','quantidade','valor_pago']

        widgets ={
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'quantidade':forms.NumberInput(attrs={'class':'form-control','min':'1'}),
            'valor_pago': forms.NumberInput(attrs={'class':'form-control','step':'0.01'})
        }

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nome']

        widgets ={
            'nome':forms.TextInput(attrs={'class':'form-control'}),
        }