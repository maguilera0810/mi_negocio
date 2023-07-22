from django.contrib.auth.models import AbstractUser
from django.db import models


class Cliente(AbstractUser):
    IDENTIFICATION_TYPES = (
        ("ruc", "ruc"),
        ("cedula", "cedula"),
    )
    tipo_identificacion = models.CharField(blank=False,
                                           null=False, max_length=6)
    identificacion = models.CharField(blank=False, null=False, max_length=15)
    celular = models.CharField(blank=False, null=False, max_length=12)


class Direccion(models.Model):
    cliente = models.ForeignKey(to=Cliente,
                                on_delete=models.CASCADE)
    provincia = models.CharField(blank=False, null=False, max_length=30)
    ciudad = models.CharField(blank=False, null=False, max_length=30)
    calle_principal = models.CharField(blank=False, null=False, max_length=30)
    calle_secundaria = models.CharField(blank=False, null=False, max_length=30)
    telefono = models.CharField(blank=False, null=False, max_length=12)
    celular = models.CharField(blank=False, null=False, max_length=12)
    codigo_postal = models.IntegerField(blank=False, null=False)
