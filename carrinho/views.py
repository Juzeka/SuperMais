from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from carrinho.carrinho_compra import Carrinho
from carrinho.forms import CarrinhoProdutoForm
from dashboard.models import Produto


@require_POST
def carrinho_add(request, id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id)

    form = CarrinhoProdutoForm(request.POST)
    if form.is_valid():
        data_produto = form.cleaned_data
        carrinho.add(
            produto=produto,
            qntd=data_produto['quantidade'],
            sobrepor_qntd=data_produto['sobrepor_qntd'],
        )
    messages.add_message(request, messages.SUCCESS, 'Produto adicionado!')
    return redirect('carrinho_detalhe')


@require_POST
def carrinho_delete(request, id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id)

    carrinho.delete(produto)
    messages.add_message(request, messages.SUCCESS, 'Produto deletado!')
    return redirect('carrinho_detalhe')


def carrinho_detalhe(request):
    contexto = {}
    carrinho = Carrinho(request)
    contexto['carrinho'] = carrinho

    return render(request,'carrinho/carrinho_detalhe.html',contexto)