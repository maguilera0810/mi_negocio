from django.urls import path

from api.v1.management.handlers.client_handler import ClientHandler

urlpatterns = [
    path('client/', ClientHandler.as_view({'get': 'list',
                                             'post': 'create'}), name='client'),
    path('client/<int:id>', ClientHandler.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'delete'}), name='client_id'),
]
