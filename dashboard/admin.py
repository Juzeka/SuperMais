from django.contrib import admin
from dashboard.models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','quantidade','valor_pago','preco_medio','data_criada','data_modificacao','status']
