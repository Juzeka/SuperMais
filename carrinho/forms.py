from django import forms


PRODUTO_QUANTIDADE = [(i, str(i)) for i in range(1,51)]

class CarrinhoProdutoForm(forms.Form):
    quantidade = forms.TypedChoiceField(label='Quantidade',choices=PRODUTO_QUANTIDADE,coerce= int)#ecolha da quantidade de produto
    sobrepor_qntd = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    widgets={
        'quantidade': forms.NumberInput(attrs={'class':'form-control','min':'1','max':'50'}),
    }