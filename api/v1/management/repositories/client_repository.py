from contextlib import suppress

from apps.management.models import Client


class ClientRepository:

    @staticmethod
    def get_one(id: int):
        with suppress(Client.DoesNotExist):
            return Client.objects.get(id=id)

    @staticmethod
    def get_all(filters: dict = None):
        if not filters:
            filters = {}
        print(filters)
        return Client.objects.filter(**filters).order_by("id")
