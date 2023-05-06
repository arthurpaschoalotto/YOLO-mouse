from rest_framework import viewsets
from src.api import serializers
from src import models

class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset = models.Usuarios.objects.all()