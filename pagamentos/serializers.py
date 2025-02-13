from rest_framework import serializers
from .models import Cliente, Produto, Venda, VendaProduto

#login:
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


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

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                }
            }
        raise serializers.ValidationError("Credenciais inválidas")