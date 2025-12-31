from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Questa è la regola di sicurezza:
    # "Se sei autenticato fai tutto, altrimenti puoi solo leggere (ReadOnly)"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]