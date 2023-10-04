from rest_framework import serializers
from .models import Usuario, Doador, Doacao, Tipo_Doacao, Admin, Fotos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'name', 'age']

class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doador
        fields = ['id', 'cpf', 'nome', 'email', 'endereco', 'telefone']

class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['id', 'data', 'doador', 'tipo', 'quantidade']

class Tipo_DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Doacao
        fields = ['id', 'nome']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'email', 'nome', 'senha']

class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = '__all__'

