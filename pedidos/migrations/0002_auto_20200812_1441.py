# Generated by Django 2.2.6 on 2020-08-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('P', 'Pedido realizado'), ('F', 'Fazendo'), ('E', 'Saiu para entrega')], max_length=16),
        ),
    ]
