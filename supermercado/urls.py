from django.urls import path
from .views import super_index,super_produto_detalhe

urlpatterns =[
    path('', super_index, name='super_index'),
    path('<str:nome>', super_index, name='super_index'),
    path('produto_detalhe/<int:id>', super_produto_detalhe, name='super_produto_detalhe'),

]