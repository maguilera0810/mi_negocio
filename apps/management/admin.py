from django.contrib import admin

from apps.management.models import Client, Address


class ClientAdmin(admin.ModelAdmin):
    ...


class DireccionAdmin(admin.ModelAdmin):
    ...


admin.site.register(Client, ClientAdmin)
admin.site.register(Address, ClientAdmin)
