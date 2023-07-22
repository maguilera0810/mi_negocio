from django.urls import include, path

urlpatterns = [
    path('management/', include('api.v1.management.routes')),
]
