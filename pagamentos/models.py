from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    contato = models.CharField(max_length=20)
    endereco = models.TextField()

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda  = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class  Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto, through='VendaProduto')
    data_compra = models.DateField(auto_now_add=True)
    data_pagamento = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f'Vendas {self.id} - {self.cliente.nome}'
    
class VendaProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade}x'