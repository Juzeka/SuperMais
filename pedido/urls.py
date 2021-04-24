from django.urls import path
from .views import finalizar_pedido,finalizado_pedido

urlpatterns =[
    path('finalizar/', finalizar_pedido, name='finalizar_pedido'),
    path('finalizado', finalizado_pedido, name='finalizado_pedido'),
]