# Generated by Django 3.2 on 2021-04-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210421_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor Pago'),
        ),
    ]
