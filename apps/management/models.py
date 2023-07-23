from django.contrib.auth.models import AbstractUser
from django.db import models
from mi_negocio.enums import IdentificationType


class Client(AbstractUser):
    IDENTIFICATION_TYPES = (
        (IdentificationType.RUC.value, IdentificationType.RUC.value),
        (IdentificationType.DNI.value, IdentificationType.DNI.value),
    )
    identification_type = models.CharField(blank=False, null=False,
                                           choices=IDENTIFICATION_TYPES, max_length=6)
    identification = models.CharField(blank=False, null=False,
                                      max_length=15, unique=True)
    cellphone = models.CharField(blank=False, null=False, max_length=30)

    def save(self, *args, **kwargs):
        self.username = self.email
        super(Client, self).save(*args, **kwargs)


class Address(models.Model):
    client = models.ForeignKey(to=Client,
                               on_delete=models.CASCADE)
    province = models.CharField(blank=False, null=False, max_length=50)
    city = models.CharField(blank=False, null=False, max_length=50)
    address = models.CharField(blank=False, null=False, max_length=150)
    is_matriz = models.BooleanField(default=False)
