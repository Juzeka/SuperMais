from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from dashboard.models import Produto, Categoria
from carrinho.forms import CarrinhoProdutoForm


def paginacao(request, model, qnd=10):
    paginacao = Paginator(model, qnd)
    paginas = request.GET.get('p')
    model = paginacao.get_page(paginas)
    return model


def super_index(request, nome=None):
    contexto = {}
    nome_cat = None
    produtos = Produto.objects.all().order_by('-id')
    categorias = Categoria.objects.all()

    if nome:
        nome_cat = get_object_or_404(Categoria, nome=nome)
        produtos = Produto.objects.filter(categoria=nome_cat)

    produtos = paginacao(request,produtos,20)
    
    contexto['categorias'] = categorias
    contexto['categoria'] = nome_cat
    contexto['produtos'] = produtos

    return render(request, 'supermercado/super_index.html', contexto)



def super_produto_detalhe(request,id):
    contexto = {}
    produto = get_object_or_404(Produto,id=id)

    carrinho_produto_form = CarrinhoProdutoForm()
    contexto['produto'] = produto
    contexto['carrinho_form']= carrinho_produto_form
    return render(request,'supermercado/super_produto_detalhe.html', contexto)