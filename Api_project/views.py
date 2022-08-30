from django.shortcuts import render
from Tarjetas.models import Tarjeta

from Tarjetas.views import tarjetas

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
from .serializers import PrestamoSucursalSerializer
from .serializers import TarjetaSerializer
from .serializers import DireccionesSerializer 
from .serializers import  PrestamoSerializer


from .permissions import esEmpleado

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse as reverse2
from django.contrib.auth.decorators import login_required

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


class PrestamoSucursal(APIView):
    permission_classes = [permissions.IsAuthenticated, esEmpleado]
    def get(self, request, sucursal_id):
        clientes = Cliente.objects.filter(branch_id = sucursal_id)
        prestamos = []
        for cliente in clientes:
            if Prestamo.objects.filter(customer_id = cliente.customer_id).exists():
                prestamos.extend(list(Prestamo.objects.filter(customer_id = cliente.customer_id)))
        if prestamos:
            serializer = PrestamoSucursalSerializer(prestamos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('No se hicieron prestamos en esta sucursal', status=status.HTTP_404_NOT_FOUND)


class SucursalLists(APIView):
    def get(self, request):
        sucursal = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursal,many=True)
        if sucursal:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# obtenter tarjeras asocidas
class TarjetasAsociadas(APIView):
    serializer_class = TarjetaSerializer

    def get_queryset(self):
        queryset = Tarjeta.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = queryset.filter(card_customer=customer_id)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    card_customer_id=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'partial_update':
            self.permission_classes = [esEmpleado]
        return super().get_permissions()

# prueba de direccion 

class DireccionesaModificar(APIView):
    serializer_class = DireccionesSerializer

    def get_queryset(self):
        queryset = Direcciones.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = queryset.filter(address_customer=customer_id)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    address_customer=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'partial_update':
            self.permission_classes = [esEmpleado]
        return super().get_permissions()



class Prestamo(APIView):
    serializer_class = PrestamoSerializer
    queryset = Prestamo.objects.all()

    def get_queryset(self):
        queryset = Prestamo.objects.all()
        sucursal_id = self.request.query_params.get('sucursal_id', None)
        if sucursal_id is not None:
            clientes = Cliente.objects.filter(branch_id=sucursal_id)
            queryset = queryset.filter(customer_id__in=clientes)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    customer_id=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            self.permission_classes = [esEmpleado]
        return super().get_permissions()


class ClienteVista(APIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        queryset = Cliente.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = queryset.filter(customer_id=customer_id)
        if self.request.user.is_authenticated:
            if not self.request.user.user.is_employee:
                queryset = queryset.filter(
                    customer_id=self.request.user.user.customer_id)
        return queryset

    def get_permissions(self):
        if self.action == 'partial_update':
            self.permission_classes = [esEmpleado]
        return super().get_permissions()
