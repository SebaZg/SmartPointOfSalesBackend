from rest_framework import serializers
from core.models import Venta, Detalle_Venta, Medio_Pago

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields =['id_venta','monto','medioPago','fecha','cliente']

class Detalle_VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Venta
        fields = ['id_detalle_venta','producto','venta']

class Medio_PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio_Pago
        fields = ['id_medio_pago','nombre']