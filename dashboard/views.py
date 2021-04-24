from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms import ProdutoForm, CategoriaForm
from dashboard.models import Produto, Categoria
from pedido.forms import PedidoForm, ItemPedidoForm
from pedido.models import Pedido, ItemPedido


def dash_index(request):
    return render(request, 'dashboard/dash_index.html')


#---------Categoria----------#
def get_instacia_categoria(request,id):
    contexto = {}
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)

    contexto['form'] = form
    contexto['categoria'] = categoria

    return contexto


def dash_categorias(request):
    contexto = {}
    categorias = Categoria.objects.all().order_by('-id')
    form = ProdutoForm(request.POST)

    contexto['categorias'] = categorias
    if request.method != 'POST':
        contexto['form'] = form
        return render(request, 'dashboard/categorias/dash_categorias.html', contexto)

    return render(request, 'dashboard/categorias/dash_categorias.html', contexto)


def dash_nova_categoria(request):
    contexto = {}
    form = CategoriaForm(request.POST)
    contexto['form'] = form

    if request.method == 'POST':
        rs_nome = str(request.POST.get('nome')).upper()
        nome_categoria_check = Categoria.objects.filter(nome=rs_nome).exists()

        if nome_categoria_check == False:
            if form.is_valid():
                form.save()
                return redirect('dash_categorias')
        else:
            print('ERRO: ja exite, recomentdo que ultilize a opção ABASTECER')
            return redirect('dash_categorias')

    else:
        return render(request, 'dashboard/produtos/dash_produto_detalhes.html', contexto)


def dash_categoria_update(request,id):
    form = get_instacia_categoria(request, id)['form']

    if request.method == 'POST':
        if form.is_valid():
            form_update = form.save(commit=False)
            form_update.nome = str(form_update.nome).upper()
            form_update.save()
            return redirect('dash_categorias')
    else:
        return render(request, 'dashboard/categorias/dash_categoria_detalhes.html', get_instacia_categoria(request, id))


def dash_categoria_del(request,id):

    if request.method == 'POST':
        get_instacia_categoria(request, id)['categoria'].delete()
        return redirect('dash_categorias')
    else:
        return render(request, 'dashboard/categorias/dash_categoria_conf_del.html', get_instacia_categoria(request, id))




#----------Progutos-------------#
def calc_vl_medio(request):

    rq_quantidade = request.POST.get('quantidade')
    rq_valor_medio = request.POST.get('valor_pago')
    calc_valor_medio = float(rq_valor_medio) / float(rq_quantidade)

    return calc_valor_medio


def get_instacia(request,id):
    contexto = {}
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    contexto['form'] = form
    contexto['produto'] = produto

    return contexto


def dash_produtos(request):
    contexto = {}
    produtos = Produto.objects.all().order_by('-id')
    form = ProdutoForm(request.POST)

    contexto['produtos'] = produtos
    if request.method != 'POST':
        contexto['form'] = form
        return render(request, 'dashboard/produtos/dash_produtos.html', contexto)

    return render(request, 'dashboard/produtos/dash_produtos.html', contexto)

def dash_nova_carga_produto(request,id):
    produto = get_instacia(request,id)['produto']
    produto_old = {'id_produto':produto.id,'id_categoria':produto.categoria.id, 'id_nome':produto.nome, 'id_quantidade':produto.quantidade, 'id_valor_pago':produto.valor_pago}
    form = get_instacia(request,id)['form']

    rs_nome=request.POST.get('nome')
    rs_categoria=request.POST.get('categoria')

    if request.method == 'POST':
        if rs_nome == produto_old['id_nome'] and int(rs_categoria) == produto_old['id_categoria']:
            if form.is_valid():
                nova_carga = form.save(commit=False)
                nova_carga.quantidade += produto_old['id_quantidade']
                nova_carga.valor_pago += produto_old['id_valor_pago']
                nova_carga.preco_medio =nova_carga.valor_pago / nova_carga.quantidade
                nova_carga.status = True
                nova_carga.save()
                return redirect('dash_produtos')
        else:
            #menssagem de error
            print('Categoria e Nome do produto não pode ser alterado')
            return render(request,'dashboard/produtos/dash_nova_carga_produto.html',get_instacia(request,id))
    else:
        print('else')
        return render(request,'dashboard/produtos/dash_nova_carga_produto.html',get_instacia(request,id))


def dash_novo_produto(request):
    contexto= {}
    form = ProdutoForm(request.POST)
    contexto['form']= form

    if request.method == 'POST':
        rs_nome = str(request.POST.get('nome')).upper()
        nome_produto_check =Produto.objects.filter(nome=rs_nome).exists()

        if nome_produto_check == False:
            if form.is_valid():
                form_data = form.save(commit=False)
                form_data.nome = rs_nome
                form_data.preco_medio = calc_vl_medio(request)
                form_data.save()
                print('Salvei pq nao exite nenhum produto com esse nome')
                return redirect('dash_produtos')
        else:
            print('ERRO: ja exite, recomentdo que ultilize a opção ABASTECER')
            return redirect('dash_produtos')
    else:
        return render(request, 'dashboard/produtos/dash_produto_detalhes.html', contexto)


def dash_produto_update(request,id):
    form = get_instacia(request, id)['form']

    if request.method == 'POST':
        if form.is_valid():
            form_update = form.save(commit=False)
            form_update.nome = str(form_update).upper()
            form_update.preco_medio = calc_vl_medio(request)
            form_update.save()
            return redirect('dash_produtos')
    else:
        return render(request, 'dashboard/produtos/dash_produto_detalhes.html', get_instacia(request,id))


def dash_produto_del(request,id):

    if request.method == 'POST':
        get_instacia(request,id)['produto'].delete()
        return redirect('dash_produtos')
    else:
        return render(request,'dashboard/produtos/dash_produto_conf_del.html',get_instacia(request,id))



# ---------Itens do pedidos ----------#
def itens_list(request):
    contexto = {}
    itens = ItemPedido.objects.all().order_by('-id')

    contexto['itens'] = itens
    return render(request, 'dashboard/itens/dash_itens.html',contexto)


def item_detalhe(request,id):
    contexto={}
    item = get_object_or_404(ItemPedido, id=id)

    contexto['item'] = item
    return render(request,'dashboard/itens/dash_item_detalhe.html',contexto)


def item_del(request,id):
    item = get_object_or_404(ItemPedido, id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('itens_list')

    return render(request,'dashboard/itens/dash_item_conf_del.html',{'item':item})


def item_update(request,id):
    contexto ={}
    item = get_object_or_404(ItemPedido, id=id)
    form = ItemPedidoForm(request.POST or None, instance=item)

    contexto['item'] = item
    contexto['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pedidos_list')
    else:
        return render(request,'dashboard/itens/dash_item_update.html', contexto)


# ---------Pedidos ----------#
def pedidos_list(request):
    contexto = {}
    pedidos = Pedido.objects.filter(pago=True).order_by('-id')

    contexto['pedidos'] = pedidos
    return render(request, 'dashboard/pedidos/dash_pedidos.html',contexto)


def pedido_detalhe(request, id):
    contexto = {}
    pedido = get_object_or_404(Pedido, id=id)
    pedido_itens = ItemPedido.objects.filter(pedido=pedido.id)

    contexto['pedido'] = pedido
    contexto['itens'] = pedido_itens
    return render(request,'dashboard/pedidos/dash_pedido_detalhe.html',contexto)


def pedido_update(request,id):
    contexto ={}
    pedido = get_object_or_404(Pedido, id=id)
    form = PedidoForm(request.POST or None, instance=pedido)

    contexto['pedido'] = pedido
    contexto['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pedidos_list')
    else:
        return render(request,'dashboard/pedidos/dash_pedido_update.html', contexto)


def pedido_del(request,id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos_list')

    return render(request,'dashboard/pedidos/dash_pedido_conf_del.html',{'pedido':pedido})


