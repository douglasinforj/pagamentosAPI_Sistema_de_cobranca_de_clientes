from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer, ProdutoSerializer, VendaSerializer
from .models import Cliente, Produto, Venda


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer