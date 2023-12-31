from django.urls import path

from api.v1.management.handlers.client_handler import ClientHandler
from api.v1.management.handlers.address_handler import AddressHandler

urlpatterns = [
    path('client/', ClientHandler.as_view({'get': 'list',
                                           'post': 'create'}), name='client'),
    path('client/<int:id>', ClientHandler.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'delete': 'delete'}), name='client_id'),
]
urlpatterns += [
    path('address/', AddressHandler.as_view({'get': 'list',
                                             'post': 'create'}), name='address'),
    path('address/<int:id>', AddressHandler.as_view({'get': 'retrieve',
                                                     'put': 'update',
                                                     'delete': 'delete'}), name='address_id'),
]
