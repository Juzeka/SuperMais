from django.urls import path
from .views import *



urlpatterns =[
    path('', dash_index, name='dash_index'),
    path('produtos/', dash_produtos, name='dash_produtos'),
    path('produtos/novo', dash_novo_produto, name='dash_novo_produto'),
    path('produtos/alterar/<int:id>', dash_produto_update, name='dash_produto_update'),
    path('produtos/deletar/<int:id>', dash_produto_del, name='dash_produto_del'),
    path('produtos/abastecimento/<int:id>', dash_nova_carga_produto, name='dash_nova_carga_produto'),

    path('categorias/', dash_categorias, name='dash_categorias'),
    path('categorias/novo', dash_nova_categoria, name='dash_nova_categoria'),
    path('categorias/alterar/<int:id>', dash_categoria_update, name='dash_categoria_update'),
    path('categorias/deletar/<int:id>', dash_categoria_del, name='dash_categoria_del'),

    path('pedidos/', pedidos_list, name='pedidos_list'),
    path('pedidos/detalhe/<int:id>', pedido_detalhe, name='pedido_detalhe'),
    path('pedidos/alterar/<int:id>', pedido_update, name='pedido_update'),
    path('pedidos/deletar/<int:id>', pedido_del, name='pedido_del'),

    path('itens/', itens_list, name='itens_list'),
    path('itens/detalhe/<int:id>', item_detalhe, name='item_detalhe'),
    path('itens/alterar/<int:id>', item_update, name='item_update'),
    path('itens/deletar/<int:id>', item_del, name='item_del'),
]
