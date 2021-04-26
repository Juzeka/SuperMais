from django.contrib.auth.context_processors import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from pedido.models import Pedido, ItemPedido


def paginacao(request, model, qnd=10):
    paginacao = Paginator(model, qnd)
    paginas = request.GET.get('p')
    model = paginacao.get_page(paginas)
    return model


@login_required(redirect_field_name='login')
def dash_user_index(request):
    return render(request,'dashboarduser/dash_user_index.html')


@login_required(redirect_field_name='login')
def dash_user_pedidos(request):
    contexto ={}
    pedidos= Pedido.objects.filter(cliente= auth(request).get('user')).order_by('-id')

    contexto['pedidos'] = paginacao(request,pedidos)
    print(auth(request).get('user'))
    return render(request,'dashboarduser/dash_user_pedidos.html',contexto)


@login_required(redirect_field_name='login')
def dash_user_pedido_detalhe(request,id):
    contexto ={}
    pedido= get_object_or_404(Pedido, id=id)
    itens =  ItemPedido.objects.filter(pedido= pedido.id).order_by('-id')

    contexto['pedido'] = pedido
    contexto['itens'] = itens

    return render(request,'dashboarduser/dash_user_pedido_detalhe.html',contexto)
