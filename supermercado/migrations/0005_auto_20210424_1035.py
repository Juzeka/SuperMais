# Generated by Django 3.2 on 2021-04-24 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermercado', '0004_itempedido_pedido'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemPedido',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]