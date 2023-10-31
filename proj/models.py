from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + str(self.age)
    
class Doador(models.Model):
    cpf = models.CharField(max_length=15)
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    endereco = models.CharField(max_length=500)
    telefone = models.CharField(max_length=50)

class Doacao(models.Model):
    data = models.DateField()
    doador = models.ForeignKey(
        'Doador', on_delete=models.CASCADE)
    tipo = models.ForeignKey(
        'Tipo_Doacao', on_delete=models.CASCADE)
    quantidade = models.IntegerField()

class Tipo_Doacao(models.Model):
    nome = models.CharField(max_length=100)

class Admin(models.Model):
    email = models.CharField(max_length=150)
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)

class Fotos(models.Model):
    data = models.DateField()
    desc = models.CharField(max_length=1000)
    link1 = models.ImageField(upload_to='images/')
    link2 = models.ImageField(upload_to='images/')
    link3 = models.ImageField(upload_to='images/')

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    assunto = models.CharField(max_length=700)
    email = models.EmailField()
    mensagem = models.TextField()

# class Image(models.Model):
#     file = models.ImageField(upload_to='images/')
   
    

    