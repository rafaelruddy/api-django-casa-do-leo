from django.forms import ValidationError
from django.contrib.auth import authenticate, login
from .models import Usuario, Doador, Doacao, Fotos, Tipo_Doacao, Contato, Admin, AdminProfile
from .serializers import UsuarioSerializer, DoadorSerializer, DoacaoSerializer, FotosSerializer, Tipo_DoacaoSerializer, ContatoSerializer, AdminSerializer, AdminInfoSerializer, LoginSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.conf import settings
from rest_framework.authentication import SessionAuthentication

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoadorViewSet(viewsets.ModelViewSet):
    queryset = Doador.objects.all()
    serializer_class = DoadorSerializer
    authentication_classes = [SessionAuthentication]  
    permission_classes = [IsAuthenticated] 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        doacoes = Doacao.objects.filter(doador=instance)
        serializer_doacao = DoacaoSerializer(doacoes, many=True)
        data['doacoes'] = serializer_doacao.data
        return Response(data)

class DoacaoViewSet(viewsets.ModelViewSet):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def infos(self, request, pk=None):
        doadores = Doador.objects.all()
        tipo_doacoes = Tipo_Doacao.objects.all()

        serializer_doadores = DoadorSerializer(doadores, many=True)
        serializer_tipo_doacao = Tipo_DoacaoSerializer(tipo_doacoes, many=True)
        status_code = status.HTTP_201_CREATED


        return Response({
            'doadores': serializer_doadores.data,
            'tipo_doacoes': serializer_tipo_doacao.data
        }, status=status_code)


class TipoDoacaoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Doacao.objects.all()
    serializer_class = Tipo_DoacaoSerializer
    authentication_classes = [SessionAuthentication]  
    permission_classes = [IsAuthenticated] 


class AdminViewSet(viewsets.ModelViewSet):
    queryset = AdminProfile.objects.all()
    serializer_class = AdminInfoSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        # Retorne uma resposta de erro indicando que o método POST não é permitido
        return Response(
            {"message": "Método POST não permitido nesta rota."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    @action(detail=False, methods=['post'], serializer_class = AdminSerializer)
    def register(self, request, pk=None):
        serializer = AdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'message': 'User registered  successfully',
        }
        
        return Response(response, status=status_code)
    
    @action(detail=False, methods=['post'], serializer_class = LoginSerializer)
    def login(self, request, pk=None):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            response = Response({'message':"Usuario logado com sucesso."}, status=status.HTTP_200_OK)
            return response
        return Response({'message': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
    
class FotosViewSet(viewsets.ModelViewSet):
    queryset = Fotos.objects.all()
    serializer_class = FotosSerializer
    permission_classes = [permissions.AllowAny]

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            nome = serializer.validated_data.get('nome')
            assunto = serializer.validated_data.get('assunto')
            email = serializer.validated_data.get('email')
            mensagem = serializer.validated_data.get('mensagem')

            try:
                validate_email(email)
            except ValidationError:
                return Response({'message': 'Email inválido.'}, status=status.HTTP_400_BAD_REQUEST)
            
            mensagem_email = f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}'
            remetente = settings. EMAIL_HOST_USER
            destinatario = settings.EMAIL_DESTINATARY   

            send_mail(assunto, mensagem_email, remetente, [destinatario])

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({'message': 'Os dados do formulário são inválidos.'}, status=status.HTTP_400_BAD_REQUEST)

    
    # def list(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def retrieve(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def update(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def partial_update(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def destroy(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
