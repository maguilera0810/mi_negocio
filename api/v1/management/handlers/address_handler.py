from rest_framework import status
from rest_framework.response import Response

from api.v1.management.services.address_service import AddressService
from api.v1.management.serializers.address_serializer import AddressSerializer
from mi_negocio.views import BaseViewSet


class AddressHandler(BaseViewSet):

    def retrieve(self, request, id):
        srv = AddressService()
        if not (address := srv.get_one(id)):
            return Response({"error": "Address no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializer(address, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        srv = AddressService()
        addresss = srv.get_all(filters=request.GET)
        serializer = AddressSerializer(addresss, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        serializer = AddressSerializer(data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        srv = AddressService()
        if not (address := srv.get_one(id)):
            return Response({"error": "Address no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = AddressSerializer(address, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def delete(self, request, id):
        srv = AddressService()
        if not (address := srv.get_one(id)):
            return Response({"error": "Address no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        address.delete()
        return Response({}, status=status.HTTP_200_OK)
