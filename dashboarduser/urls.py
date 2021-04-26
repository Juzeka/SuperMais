from django.urls import path
from .views import dash_user_index,dash_user_pedidos,dash_user_pedido_detalhe

urlpatterns =[
    path('', dash_user_index, name='dash_user_index'),
    path('meus_pedidos/', dash_user_pedidos, name='dash_user_pedidos'),
    path('meu_pedido/detalhe/<int:id>', dash_user_pedido_detalhe, name='dash_user_pedido_detalhe'),
]