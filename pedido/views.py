from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from carrinho.carrinho_compra import Carrinho
from dashboard.models import Produto
from pedido.forms import PedidoForm
from pedido.models import ItemPedido


#----------Pedidos---------#
def finalizar_pedido(request):
    contexto = {}
    carrinho = Carrinho(request)

    contexto['carrinho'] = carrinho
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if carrinho:
            if form.is_valid():
                pedido = form.save()
                for item in carrinho:

                    id_produto_carrinho =item['produto'].id
                    produto = get_object_or_404(Produto, id=id_produto_carrinho)
                    if produto.quantidade >= item['qntd'] and produto.quantidade > 0 and produto.status == True:
                        quantidade_nova = produto.quantidade - int(item['qntd'])
                        valor_pago_novo = produto.valor_pago - item['preco_medio']

                        if quantidade_nova == 0:
                            Produto.objects.filter(id =id_produto_carrinho).update(quantidade = quantidade_nova, valor_pago=valor_pago_novo, status=False)

                        elif quantidade_nova >0:
                            Produto.objects.filter(id =id_produto_carrinho).update(quantidade = quantidade_nova, valor_pago=valor_pago_novo)

                        else:
                            messages.add_message(request, messages.ERROR, 'Um dos produtos sem quantidade diponível!')
                            return redirect('finalizar_pedido')

                        ItemPedido.objects.create(pedido=pedido, produto=item['produto'],preco=item['preco_medio'], quantidade= item['qntd'])

                    else:
                        messages.add_message(request, messages.ERROR, 'Um dos produtos sem estoque diponível!')
                        return redirect('finalizar_pedido')

                messages.add_message(request, messages.SUCCESS, 'Compra feita com sucesso!')
                return redirect('finalizado_pedido')

        else:
            messages.add_message(request, messages.ERROR, 'Manipulação inválida!')
            return HttpResponseRedirect(reversed('super_index'))

    else:
        form = PedidoForm()
        contexto['form'] = form
        return render(request,'pedido/pedido_finalizar.html',contexto)


def finalizado_pedido(request):
    carrinho = Carrinho(request)
    carrinho.clean()
    return render(request,'pedido/pedido_finalizado.html',{'carrinho':carrinho})

def cleam(request):
    carrinho = Carrinho(request)
    carrinho.clean()
    return redirect('super_index')