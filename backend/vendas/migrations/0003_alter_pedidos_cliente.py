# Generated by Django 4.1.7 on 2023-03-09 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_clientes_pedidos_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.clientes'),
        ),
    ]
