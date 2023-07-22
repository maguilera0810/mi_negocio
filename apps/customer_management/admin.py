from django.contrib import admin

from apps.customer_management.models import Cliente, Direccion


class ClienteAdmin(admin.ModelAdmin):
    ...


class DireccionAdmin(admin.ModelAdmin):
    ...


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Direccion, ClienteAdmin)
