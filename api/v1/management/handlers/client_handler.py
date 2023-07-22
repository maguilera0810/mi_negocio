from rest_framework import status
from rest_framework.response import Response

from api.v1.management.services.client_service import ClientService
from api.v1.management.serializers.client_serializer import ClientSerializer
from api.v1.management.serializers.address_serializer import AddressSerializer
from mi_negocio.views import BaseViewSet


class ClientHandler(BaseViewSet):

    def retrieve(self, request, id):
        srv = ClientService()
        if not (client := srv.get_one(id)):
            return Response({"error": "Client no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(client, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        srv = ClientService()
        clients = srv.get_all(filters=request.GET.dict())
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        address = data["main_address"]
        client_serializer = ClientSerializer(data=data, partial=False)
        if not client_serializer.is_valid():
            return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        client = client_serializer.save()
        address["client"] = client.id
        address_serializer = AddressSerializer(data=address, partial=False)
        if not address_serializer.is_valid():
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        address_serializer.save()
        return Response(client_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        srv = ClientService()
        if not (client := srv.get_one(id)):
            return Response({"error": "Client no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = ClientSerializer(client, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def delete(self, request, id):
        srv = ClientService()
        if not (client := srv.get_one(id)):
            return Response({"error": "Client no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        client.delete()
        return Response({}, status=status.HTTP_200_OK)
