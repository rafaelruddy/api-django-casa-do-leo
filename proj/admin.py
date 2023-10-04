from django.contrib import admin
from .models import Usuario, Doacao, Doador, Admin, Fotos

admin.site.register(Usuario)
admin.site.register(Doacao)
admin.site.register(Doador)
admin.site.register(Admin)
admin.site.register(Fotos)