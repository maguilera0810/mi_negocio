from unittest import mock

from django.http import QueryDict
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.v1.management.handlers.client_handler import ClientHandler
from api.v1.management.handlers.address_handler import AddressHandler
from apps.management.models import Address, Client
from tests.factories.management import (AddressFactory, AddressModelFactory,
                                        ClientModelFactory)


class ManagementTestCase(TestCase):
    def setUp(self):
        self.client_handler = ClientHandler()
        self.address_handler = AddressHandler()
        self.client = APIClient()

    def test_client_create(self):
        client_data = ClientModelFactory()
        address_data = AddressFactory(is_matriz=True)
        data = {
            "email": client_data.email,
            "first_name": client_data.first_name,
            "last_name": client_data.last_name,
            "identification_type": client_data.identification_type,
            "identification": client_data.identification,
            "cellphone": client_data.cellphone,
            "main_address": {
                "province": address_data.province,
                "city": address_data.city,
                "address": address_data.address,
                "is_matriz": address_data.is_matriz,
            }
        }
        request = mock.Mock(data=data)
        response = self.client_handler.create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Client.objects.filter(
            identification=client_data.identification).exists())
        self.assertTrue(Address.objects.filter(
            client__identification=client_data.identification).exists())

    def test_client_retrieve(self):
        client_data = ClientModelFactory()
        client_data.save()
        address_data = AddressModelFactory(client=client_data,
                                           is_matriz=True)
        address_data.save()
        request = mock.Mock()
        response = self.client_handler.retrieve(request, client_data.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_list(self):
        clients_data = []
        n = 5
        import json
        for _ in range(n):
            client_data = ClientModelFactory()
            client_data.save()
            address_data = AddressModelFactory(client=client_data,
                                               is_matriz=True)
            address_data.save()
            clients_data.append(client_data)
        params = QueryDict(mutable=True)
        params["identification"] = clients_data[0].identification
        request = mock.Mock(GET=params)
        response = self.client_handler.list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["identification"],
                         clients_data[0].identification)
        request = mock.Mock(GET=QueryDict(""))
        response = self.client_handler.list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(clients_data))

    def test_client_update(self):
        client_data = ClientModelFactory(email="email_1@example.com",
                                         first_name="first_name_1",
                                         last_name="last_name_1",
                                         identification_type="RUC",
                                         identification="9999999999001",
                                         cellphone="+593999999999")
        client_data.save()
        address_data = AddressModelFactory(client=client_data,
                                           is_matriz=True)
        address_data.save()
        data = {
            "email": "email_2@example.com",
            "first_name": "first_name_2",
            "last_name": "last_name_2",
            "identification_type": "DNI",
            "identification": "8888888888",
            "cellphone": "0998574859",
        }
        request = mock.Mock(data=data)
        response = self.client_handler.update(request, client_data.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], data["email"])
        self.assertNotEqual(response.data["email"], client_data.email)

    def test_client_delete(self):
        client_data = ClientModelFactory()
        client_data.save()
        address_data = AddressModelFactory(client=client_data,
                                           is_matriz=True)
        address_data.save()
        request = mock.Mock()
        response = self.client_handler.delete(request, client_data.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Client.objects.filter(
            identification=client_data.identification).exists())

    def test_address_create(self):
        client_data = ClientModelFactory()
        client_data.save()
        AddressModelFactory(client=client_data,
                            is_matriz=True).save()
        address_data_2 = AddressFactory(is_matriz=False)
        data = {
            "client": client_data.id,
            "province": address_data_2.province,
            "city": address_data_2.city,
            "address": address_data_2.address,
            "is_matriz": address_data_2.is_matriz,
        }
        request = mock.Mock(data=data)
        response = self.address_handler.create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.filter(
            client__identification=client_data.identification).count(), 2)

    def test_address_list(self):
        clients_data = []
        for i in range(3):
            client_data = ClientModelFactory()
            client_data.save()
            AddressModelFactory(client=client_data,
                                is_matriz=True).save()
            for i in range(4):
                AddressModelFactory(client=client_data,
                                    is_matriz=False).save()
            clients_data.append(client_data)
        params = QueryDict(mutable=True)
        params["client"] = client_data.id
        request = mock.Mock(GET=params)
        response = self.address_handler.list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        request = mock.Mock(GET=QueryDict(""))
        response = self.address_handler.list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 15)
