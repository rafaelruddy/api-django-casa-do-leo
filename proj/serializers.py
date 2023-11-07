from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from .models import Usuario, Doador, Doacao, Tipo_Doacao, Admin, Fotos, Contato, AdminProfile

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'name', 'age']

class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doador
        fields = ['id', 'cpf', 'nome', 'email', 'endereco', 'telefone']

class DoacaoSerializer(serializers.ModelSerializer):
    nome_doador = serializers.SerializerMethodField()
    tipo_doacao = serializers.SerializerMethodField()
    class Meta:
        model = Doacao
        fields = ['id', 'data', 'nome_doador', 'tipo_doacao', 'quantidade']

    def get_nome_doador(self, obj):
        return obj.doador.nome
    
    def get_tipo_doacao(self, obj):
        return obj.tipo.nome

class Tipo_DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Doacao
        fields = ['id', 'nome']

class AdminSerializer(serializers.ModelSerializer):
    nome = serializers.CharField()

    class Meta:
        model = Admin
        fields = ('email', 'password', 'nome')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Admin.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        AdminProfile.objects.create(
            user=user,
            nome= validated_data['nome']
        )


        user.set_password(validated_data['password'])
        user.save()
        return user
    

class AdminInfoSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    class Meta:
        model = AdminProfile
        fields = ('email', 'nome')

    def get_email(self, obj):
        return obj.user.email


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('email', 'password')

class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = '__all__'

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'nome', 'assunto', 'email', 'mensagem']
