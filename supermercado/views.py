from django.shortcuts import render
from dashboard.models import Produto, Categoria


def super_index(request):
    contexto = {}
    produtos = Produto.objects.all().order_by('-id')
    categorias = Categoria.objects.all()

    contexto['produtos'] = produtos
    contexto['categorias'] = categorias
    return render(request,'supermercado/super_index.html', contexto)



