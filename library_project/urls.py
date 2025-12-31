"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet

# --- IMPORTA LE VISTE JWT ---
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 1. Creiamo il Router
router = DefaultRouter()

# 2. Registriamo la nostra app nel router
# Il primo argomento r'books' definisce il prefisso dell'URL
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 3. Includiamo gli URL generati dal router
    # Usiamo 'api/' come prefisso per tenere tutto ordinato
    path('api/', include(router.urls)), 

    # Attiva il tasto "Log in" nell'interfaccia
    path('api-auth/', include('rest_framework.urls')),
    # Questo è l'endpoint per fare il LOGIN (ottieni il token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Questo serve per rinnovare il token quando scade (Refresh)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
