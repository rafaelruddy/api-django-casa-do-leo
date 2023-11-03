"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from proj import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from proj.views import  FotosViewSet, DoacaoViewSet, DoadorViewSet, TipoDoacaoViewSet, ContatoViewSet, AdminViewSet

router = routers.DefaultRouter()
router.register('fotos', FotosViewSet, basename='foto')
router.register('admins', AdminViewSet, basename='admin')
router.register('doacoes', DoacaoViewSet, basename='doacao')
router.register('doadores', DoadorViewSet, basename='doadores')
router.register('tipo_doacao', TipoDoacaoViewSet, basename='tipo de doacao')
router.register('contato', ContatoViewSet, basename='contato')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



