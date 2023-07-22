from contextlib import suppress

from apps.management.models import Address


class AddressRepository:

    @staticmethod
    def get_one(id: int):
        with suppress(Address.DoesNotExist):
            return Address.objects.get(id=id)

    @staticmethod
    def get_all(filters: dict = None):
        if not filters:
            filters = {}
        return Address.objects.filter(**filters).order_by("id")
