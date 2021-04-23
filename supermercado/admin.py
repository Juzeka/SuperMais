from django.contrib import admin

from supermercado.models import Compra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'endereco']