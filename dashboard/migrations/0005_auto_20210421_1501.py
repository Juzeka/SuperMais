# Generated by Django 3.2 on 2021-04-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_produto_valor_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='preco_venda',
        ),
        migrations.AlterField(
            model_name='produto',
            name='data_criada',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='data_modificacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado'),
        ),
    ]
