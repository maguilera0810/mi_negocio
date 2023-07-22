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
        if Client.objects.filter(email=email).exists():
            raise ValidationError(
                {"email": "Ya existe un client con este correo electrónico."})
        return data

    def get_main_address(self, instance):
        if (address := Address.objects.filter(client=instance,
                                              is_matriz=True).first()):
            return AddressSerializer(address, many=False).data
