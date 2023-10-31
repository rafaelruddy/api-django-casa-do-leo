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
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from proj.views import  AdminViewSet, FotosViewSet, DoacaoViewSet, DoadorViewSet, TipoDoacaoViewSet

router = routers.DefaultRouter()
router.register('fotos', FotosViewSet, basename='foto')
router.register('admins', AdminViewSet, basename='admin')
router.register('doacoes', DoacaoViewSet, basename='doacao')
router.register('doadores', DoadorViewSet, basename='doacao')
router.register('tipo_doacao', TipoDoacaoViewSet, basename='tipo de doacao')
# router.register('image', ImageViewSet, basename='image')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('token/', TokenObtainPairView.as_view()),
    # path('token/refresh', TokenRefreshView.as_view()),
    # path('usuarios/', views.usuario_list),
    # path('usuarios/<int:id>', views.usuario_detail),
    # path('doadores/', views.doador_list),
    # path('doadores/<int:id>', views.doador_detail),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



