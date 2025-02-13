from rest_framework import serializers
from .models import Cliente, Produto, Venda, VendaProduto


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class VendaProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaProduto
        fields = '__'


    
class VendaSerializer(serializers.ModelSerializer):
    produtos = VendaProdutoSerializer(many=True, source='vendaproduto_set', read_only=True)

    class Meta:
        model = Venda
        fields = '__all__'


#LOGIN Personalizado

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)