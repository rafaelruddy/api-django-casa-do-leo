import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
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

class AdminManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Admin(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = AdminManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "login"

class AdminProfile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(Admin, on_delete=models.CASCADE, related_name='profile')
    nome = models.CharField(max_length=200)

    class Meta:
        db_table = "profile"


class Fotos(models.Model):
    data = models.DateField()
    desc = models.CharField(max_length=1000)
    link1 = models.ImageField(upload_to='images/')
    titulo = models.CharField(max_length=200)

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    assunto = models.CharField(max_length=700)
    email = models.EmailField()
    mensagem = models.TextField()

# class Image(models.Model):
#     file = models.ImageField(upload_to='images/')
   
    

    