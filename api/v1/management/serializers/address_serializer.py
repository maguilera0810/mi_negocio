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
        instance = self.instance
        data_client = data.get('client')
        if instance:
            if data_client and instance.client.id != data_client:
                client_id = data.get('client')
            else:
                client_id = instance.client.id
            instance_id = self.instance.id
        else:
            instance_id = None
            client_id = data.get('client')
        if data.get('is_matriz') and \
            Address.objects.filter(client=client_id,
                                   is_matriz=True).exclude(id=instance_id).exists():
            raise ValidationError(
                {'is_matriz': 'Ya existe una address matriz vinculada a este cliente.'})
        return data
