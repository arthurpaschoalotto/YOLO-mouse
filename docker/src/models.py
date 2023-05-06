from django.db import models

class Usuarios(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)