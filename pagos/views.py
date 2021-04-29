from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import Pago

#Response 
from rest_framework.response import Response 

#serializer import
from .serializers import PagoSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST', 'PUT'])
def pagos_arriendos(request):
    '''This function wil handle the Get, Post, Put request from the User '''
    
    if request.method == 'GET':
        pagos = Pago.objects.all()
        serializer = PagoSerializer(pagos, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            valor_dep = int(serializer.data['valorPagado'])
            if valor_dep == 1000000:
                return Response({"respuesta":"gracias por pagar todo tu arriendo"}, status=status.HTTP_201_CREATED)
            valor_res = str(1000000 - valor_dep)
            respuesta1 = "gracias por tu abono sin embargo recuerda que te hace falta pagar " + valor_res
            return Response({"respuesta": respuesta1}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = PagoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"respuesta":"gracias por pagar todo tu arriendo"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  