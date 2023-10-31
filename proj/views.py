from .models import Usuario, Doador, Doacao, Admin, Fotos, Tipo_Doacao, Contato
from .serializers import UsuarioSerializer, DoadorSerializer, DoacaoSerializer, AdminSerializer, FotosSerializer, Tipo_DoacaoSerializer, ContatoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.conf import settings


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoadorViewSet(viewsets.ModelViewSet):
    queryset = Doador.objects.all()
    serializer_class = DoadorSerializer
    permission_classes = [permissions.AllowAny]

class DoacaoViewSet(viewsets.ModelViewSet):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer
    permission_classes = [permissions.AllowAny]

class TipoDoacaoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Doacao.objects.all()
    serializer_class = Tipo_DoacaoSerializer
    permission_classes = [permissions.AllowAny]

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.AllowAny]
    
class FotosViewSet(viewsets.ModelViewSet):
    queryset = Fotos.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [permissions.AllowAny]

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            print('a')
            nome = serializer.validated_data.get('nome')
            assunto = serializer.validated_data.get('assunto')
            email = serializer.validated_data.get('email')
            mensagem = serializer.validated_data.get('mensagem')

            try:
                validate_email(email)
            except ValidationError:
                return Response({'error': 'Email inválido.'}, status=status.HTTP_400_BAD_REQUEST)
            
            mensagem_email = f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}'
            remetente = settings. EMAIL_HOST_USER
            destinatario = settings.EMAIL_DESTINATARY   

            send_mail(assunto, mensagem_email, remetente, [destinatario])

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({'error': 'Os dados do formulário são inválidos.'}, status=status.HTTP_400_BAD_REQUEST)

    
    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def usuario_list(request, format=None):
    
#     if (request.method == 'GET'):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)

#     if (request.method == 'POST'):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])        
# def usuario_detail(request,id, format=None):
    
#     try:
#         usuario = Usuario.objects.get(pk=id)
#     except Usuario.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UsuarioSerializer(usuario)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = UsuarioSerializer(usuario, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     elif request.method == 'DELETE':
#         usuario.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # doador
# @api_view(['GET', 'POST'])
# def doador_list(request, format=None):
    
#     if (request.method == 'GET'):
#         doadores = Doador.objects.all()
#         serializer = DoadorSerializer(doadores, many=True)
#         return Response(serializer.data)

#     if (request.method == 'POST'):
#         serializer = DoadorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])        
# def doador_detail(request,id, format=None):
    
#     try:
#         doador = Doador.objects.get(pk=id)
#     except Doador.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DoadorSerializer(doador)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = DoadorSerializer(doador, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     elif request.method == 'DELETE':
#         doador.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # doacao   
# @api_view(['GET', 'POST'])
# def doacao_list(request, format=None):
    
#     if (request.method == 'GET'):
#         doacoes = Doacao.objects.all()
#         serializer = DoacaoSerializer(doacoes, many=True)
#         return Response(serializer.data)

#     if (request.method == 'POST'):
#         serializer = DoacaoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])        
# def doacao_detail(request,id, format=None):
    
#     try:
#         doacao = Doacao.objects.get(pk=id)
#     except Doacao.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DoacaoSerializer(doacao)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = DoacaoSerializer(doacao, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     elif request.method == 'DELETE':
#         doacao.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # admin
# @api_view(['GET', 'POST'])
# def admin_list(request, format=None):
    
#     if (request.method == 'GET'):
#         admins = Admin.objects.all()
#         serializer = AdminSerializer(admins, many=True)
#         return Response(serializer.data)

#     if (request.method == 'POST'):
#         serializer = AdminSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])        
# def admin_detail(request,id, format=None):
    
#     try:
#         admin = Admin.objects.get(pk=id)
#     except Admin.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = AdminSerializer(admin)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = AdminSerializer(admin, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     elif request.method == 'DELETE':
#         admin.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# fotos
# @api_view(['GET', 'POST'])
# def fotos_list(request, format=None):
    
#     if (request.method == 'GET'):
#         fotos = Fotos.objects.all()
#         serializer = FotosSerializer(fotos, many=True)
#         return Response(serializer.data)

#     if (request.method == 'POST'):
#         serializer = FotosSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])        
# def fotos_detail(request,id, format=None):
    
#     try:
#         foto = Fotos.objects.get(pk=id)
#     except Fotos.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = AdminSerializer(foto)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = AdminSerializer(foto, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     elif request.method == 'DELETE':
#         foto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ImageViewSet(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     permission_classes = [permissions.AllowAny]