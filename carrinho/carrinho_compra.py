import copy
from decimal import Decimal
from django.conf import settings
from dashboard.models import Produto
from .forms import CarrinhoProdutoForm


class Carrinho(object):

    def __init__(self, request):

        self.session =request.session

        carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        if not carrinho:
            carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}
        print(f'contrutor: {carrinho}')
        self.carrinho = carrinho


    def __iter__(self):
        produto_ky = self.carrinho.keys()
        carrinho_provi = copy.deepcopy(self.carrinho)

        # obtem o objeto
        produtos = Produto.objects.filter(id__in=produto_ky)



        for produto in produtos:
            carrinho_provi[str(produto.id)]['produto'] = produto

        for item in carrinho_provi.values():
            item['preco_medio'] = Decimal(item['preco_medio'])
            item['preco_total'] = item['preco_medio'] * item['qntd']
            item['update_qnd'] = CarrinhoProdutoForm(initial={'quantidade': item['qntd'], 'sobrepor_qntd': True})
            yield item


    # soma o total de itens
    def __len__(self):
        return sum(item['qntd'] for item in self.carrinho.values())


    def add(self, produto, qntd=1, sobrepor_qntd=False):
        produto_id = str(produto.id)

        if produto_id not in self.carrinho:#add se nao existir
            self.carrinho[produto_id] = {'qntd':0, 'preco_medio': str(produto.preco_medio)}

        if sobrepor_qntd:
            self.carrinho[produto_id]['qntd'] = qntd #sobrepoe
        else:
            self.carrinho[produto_id]['qntd'] += qntd #incrementa

        self.carrinho[produto_id]['qntd'] = min(50,self.carrinho[produto_id]['qntd'])# limintando a 50

        self.save()



    def save(self):
        self.session.modified = True


    def delete(self,produto):
        produto_id = str(produto.id)

        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.save()



    #calcular custo total
    def get_preco_total(self):
        return sum(item['qntd'] * Decimal(item['preco_medio']) for item in self.carrinho.values())


    #limpar o carrinho da sessão
    def clean(self):
        del self.session[settings.CARRINHO_SESSION_ID]
        self.save()