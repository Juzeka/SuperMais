# Generated by Django 3.2 on 2021-04-24 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_produto_preco_medio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_medio',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=5, verbose_name='Preço de Venda'),
        ),
    ]