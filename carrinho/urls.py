from django.urls import path
from .views import carrinho_detalhe,carrinho_add,carrinho_delete

urlpatterns =[
    path('', carrinho_detalhe, name='carrinho_detalhe'),
    path('carrinho_add/<int:id>', carrinho_add, name='carrinho_add'),
    path('carrinho_delete/<int:id>', carrinho_delete, name='carrinho_delete'),
]