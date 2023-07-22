from rest_framework.serializers import (ModelSerializer, SerializerMethodField,
                                        ValidationError)

from api.v1.management.serializers.address_serializer import AddressSerializer
from apps.management.models import Address, Client


class ClientSerializer(ModelSerializer):
    main_address = SerializerMethodField('get_main_address')

    class Meta:
        model = Client
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'identification_type',
            'identification',
            'cellphone',
            'main_address',
        )

    def validate(self, data):
        email = data.get('email')
        instance = self.instance  # Obtener la instancia actual del cliente

        # Si es una actualización y el correo no cambió, no hay problemas
        if instance and instance.email == email:
            return data

        # Verificar si existe algún cliente diferente con el mismo correo
        if Client.objects.filter(email=email).exclude(id=instance.id if instance else None).exists():
            raise ValidationError(
                {"email": "Ya existe un cliente con este correo electrónico."})
        return data

    def get_main_address(self, instance):
        if (address := Address.objects.filter(client=instance,
                                              is_matriz=True).first()):
            return AddressSerializer(address, many=False).data
