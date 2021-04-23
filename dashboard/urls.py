from django.urls import path
from .views import dash_index, \
    dash_produtos,\
    dash_novo_produto,\
    dash_produto_update,\
    dash_produto_del,\
    dash_nova_carga_produto,\
    dash_categorias,\
    dash_nova_categoria,\
    dash_categoria_update,\
    dash_categoria_del

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
    path('produtos/deletar/<int:id>', dash_categoria_del, name='dash_categoria_del'),
]
