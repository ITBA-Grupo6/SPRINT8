from django.shortcuts import render

# Create your views here.

from .models import Cliente
from .models import Cuenta
from .models import Direcciones
from .models import TipoCliente
from .models import TipoCuenta

from .models import Empleado
from .models import ids
from .models import Movimiento
from .models import Prestamo
from .models import Sucursal

from .serializers import SucursalSerializer
from .serializers import ClienteSerializer
from .serializers import CuentaSerializer
from .serializers import PrestamoClienteSerializer
#from .permissions import esEmpleado
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse as reverse2

class DatosCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, cliente_dni):
        user = request.user 
        owner = str(cliente_dni)   
        cliente = Cliente.objects.get(customer_dni=owner)
        if (user.username == owner):
            cliente = Cliente.objects.filter(customer_dni=owner)
            serializercliente = ClienteSerializer(cliente, many=True)
            if cliente:
                return Response(serializercliente.data, status=status.HTTP_200_OK)
            return Response('No existe zcliente para este dni', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('No coincide el dni', status=status.HTTP_401_UNAUTHORIZED)

class SaldoCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, cliente_dni):
        user = request.user 
        owner = str(cliente_dni)   
        cliente = Cliente.objects.get(customer_dni=owner)
        id_cuenta = cliente.customer_id       
        if (user.username == owner):
            cuenta = Cuenta.objects.filter(account_id=id_cuenta)
            serializer = CuentaSerializer(cuenta, many=True)
            print(serializer.data[0])
            if cuenta:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('No existe cliente para este dni', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('No coincide el dni', status=status.HTTP_401_UNAUTHORIZED)

class PrestamoCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, cliente_dni):
        user = request.user 
        owner = str(cliente_dni)   
        cliente = Cliente.objects.get(customer_dni=owner)
        id_cliente = cliente.customer_id      
        cuenta = Cuenta.objects.get(account_id=id_cliente) 
        if (user.username == owner):
            id_cuenta = cuenta.customer_id
            print(id_cuenta)
            prestamo = Prestamo.objects.filter(customer_id=id_cuenta)
            serializer = PrestamoClienteSerializer(prestamo, many=True)
            if cuenta:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('No existe cliente para este dni', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('No coincide el dni', status=status.HTTP_401_UNAUTHORIZED)

class SucursalLists(APIView):
    def get(self, request):
        sucursal = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursal,many=True)
        if sucursal:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

