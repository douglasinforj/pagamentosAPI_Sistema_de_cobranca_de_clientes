import random
from faker import Faker
from decimal import Decimal
from django.utils.timezone import now, timedelta
from pagamentos.models import Cliente, Produto, Venda, VendaProduto  # Ajuste conforme o nome do seu app

fake = Faker('pt_BR')

# Criar 300 clientes
clientes = []
for _ in range(300):
    cliente = Cliente(
        nome=fake.name(),
        cpf_cnpj=fake.unique.cpf(),
        contato=fake.phone_number(),
        endereco=fake.address(),
    )
    clientes.append(cliente)

Cliente.objects.bulk_create(clientes)
clientes = list(Cliente.objects.all())  # Buscar os clientes salvos

# Criar 50 produtos de beleza
produtos_nomes = [
    "Shampoo Hidratante", "Condicionador Nutritivo", "Creme para Pentear",
    "Óleo Capilar", "Gel Fixador", "Máscara Capilar", "Perfume Feminino",
    "Perfume Masculino", "Desodorante", "Sabonete Líquido", "Hidratante Corporal",
    "Protetor Solar", "Base para Maquiagem", "Batom Matte", "Sombra para Olhos",
    "Rímel", "Esmalte", "Tônico Facial", "Creme Anti-idade", "Serum Facial",
    "Água Micelar", "Pó Compacto", "Corretivo", "Iluminador", "Blush",
    "Shampoo a Seco", "Óleo Corporal", "Sabonete Esfoliante", "Lápis de Olho",
    "Delineador", "Primer Facial", "Protetor Labial", "Spray Fixador", "Leave-in",
    "Cera Modeladora", "Lenços Demaquilantes", "Bálsamo Labial", "Creme para Olheiras",
    "Gel Redutor de Celulite", "Mousse Modeladora", "Condicionador Sem Enxágue",
    "Shampoo Anticaspa", "Máscara de Argila", "Sabonete Facial", "Tônico Capilar",
    "Fluido Termoativado", "Água Termal", "BB Cream", "CC Cream"
]

produtos = []
for nome in produtos_nomes:
    produto = Produto(
        nome=nome,
        valor_compra=Decimal(random.uniform(10, 100)).quantize(Decimal('0.01')),
        valor_venda=Decimal(random.uniform(50, 200)).quantize(Decimal('0.01')),
    )
    produtos.append(produto)

Produto.objects.bulk_create(produtos)
produtos = list(Produto.objects.all())  # Buscar os produtos salvos

# Criar 500 vendas aleatórias
vendas = []
for _ in range(500):
    cliente = random.choice(clientes)
    data_pagamento = now().date() - timedelta(days=random.randint(0, 30))  # Pagamento em até 30 dias atrás
    pago = random.choice([True, False])
    
    venda = Venda(
        cliente=cliente,
        data_pagamento=data_pagamento,
        valor_total=Decimal(0),  # Calculado depois
        pago=pago
    )
    vendas.append(venda)

Venda.objects.bulk_create(vendas)
vendas = list(Venda.objects.all())  # Buscar as vendas salvas

# Criar produtos em cada venda
venda_produtos = []
for venda in vendas:
    produtos_selecionados = random.sample(produtos, k=random.randint(1, 5))  # De 1 a 5 produtos por venda
    valor_total = Decimal(0)

    for produto in produtos_selecionados:
        quantidade = random.randint(1, 5)
        preco_unitario = produto.valor_venda
        valor_total += preco_unitario * quantidade

        venda_produto = VendaProduto(
            venda=venda,
            produto=produto,
            quantidade=quantidade,
            preco_unitario=preco_unitario
        )
        venda_produtos.append(venda_produto)

    venda.valor_total = valor_total
    venda.save()

VendaProduto.objects.bulk_create(venda_produtos)

print("✅ Banco de dados populado com sucesso!")
