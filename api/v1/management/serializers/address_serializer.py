from rest_framework.serializers import ModelSerializer, ValidationError

from apps.management.models import Address


class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'id',
            'province',
            'city',
            'address',
            'is_matriz',
            'client',
        )

    def validate(self, data):
        client = data.get('client')
        if data.get('is_matriz') and Address.objects.filter(client=client).exists():
            raise ValidationError(
                {'is_matriz': 'Ya existe una address matriz vinculada a este cliente.'})
        return data
