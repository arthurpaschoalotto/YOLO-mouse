from rest_framework import serializers
from src import models

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuarios
        field = '__all__'