from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Venta, Detalle_Venta, Medio_Pago
from .serializers import Detalle_VentaSerializer, Medio_PagoSerializer, VentaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#EndPoint de Ventas
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_ventas(request):
    """
    Lista todas las ventas realizadas
    """
    if request.method == 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#EndPoint de Detalle de las ventas
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_detalle_ventas(request):
    """ 
    Lista todos los detalle de las ventas realizadas
    """
    if request.method == 'GET':
        detalle_venta = Detalle_Venta.objects.all()
        serializer = Detalle_VentaSerializer(detalle_venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Detalle_VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#EndPoint de medio de pago
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_medio_pagos(request):
    """ 
    Lista todos los medios de pagos existetes
    """
    if request.method == 'GET':
        mediopago = Medio_Pago.objects.all()
        serializer = Medio_PagoSerializer(mediopago, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = Medio_PagoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#EndPoint de las ventas detalladas por ID
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def venta_detalle(request,id_venta):
    """ 
    Get, update o delete de una venta en especifico.
    Recibe el parametro <id_venta>
    """
    try:
        venta_detalle = Venta.objects.get(id_venta=id_venta)
    except Venta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VentaSerializer(venta_detalle)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(venta_detalle, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        venta_detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#EndPoint de los detalle_venta referenciados por ID
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_venta(request,id_detalle_venta):
    """ 
    Get, update o delete de un detalle de venta.
    Recibe el parametro <id_detalle_venta>
    """
    try:
        detalle_venta = Detalle_Venta.objects.get(id_detalle_venta=id_detalle_venta)
    except Detalle_Venta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Detalle_VentaSerializer(detalle_venta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Detalle_VentaSerializer(detalle_venta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        detalle_venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_medio_pago(request,id_medio_pago):
    """ 
    Get, update o delete de un medio de pago en especifico.
    Recibe el parametro <id_medio_pago>
    """
    try:
        medio_pago = Medio_Pago.objects.get(id_medio_pago=id_medio_pago)
    except medio_pago.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Medio_PagoSerializer(medio_pago)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Medio_PagoSerializer(medio_pago, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        medio_pago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)