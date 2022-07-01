from django.contrib import admin

from core.models import Cliente, Detalle_Venta, Medio_Pago, Producto, Venta

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Detalle_Venta)
admin.site.register(Medio_Pago)
admin.site.register(Producto)