from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer, ProdutoSerializer, VendaSerializer
from .models import Cliente, Produto, Venda

#filtros:
from rest_framework import filters
from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #filtro clientes---------------------------------------
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'cpf_cnpj']

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    #filtrando vendas por cliente e data--------------------
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente_nome']

    def get_queryset(self):
        queryset = super().get_queryset()
        cliente_id = self.request.query_params.get('cliente')
        data_inicio = self.request.query_params.get('data_inicio')
        data_fim = self.request.query_params.get('data_fim')

        if cliente_id:
            queryset = queryset.filter(cliente_id=cliente_id)
        if data_inicio and data_fim:
            queryset = queryset.filter(data_pagamento__range=[data_inicio, data_fim])

        return queryset
    
    # listar Vendas Pendentes de Pagamento
    @action(detail=False, methods=['get'])
    def pendentes(self, request):
        hoje = now().date()
        vendas_pendentes = Venda.objects.filter(Q(data_pagamento__gte=hoje) & Q(valor_total__gt=0))
        serializer = self.get_serializer(vendas_pendentes, many=True)
        return Response(serializer.data)