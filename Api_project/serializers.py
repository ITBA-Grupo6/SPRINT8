from rest_framework import serializers 
from .models import Empleado
from .models import Movimiento
from .models import Sucursal
from .models import Prestamo
from .models import Cliente
from .models import Cuenta
from .models import Direcciones
from .models import TipoCliente
from .models import TipoCuenta
from .models import Tarjeta

class ClienteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Cliente
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 
class CuentaSerializer(serializers.ModelSerializer):
     class Meta:
        model = Cuenta
        #indicamos que use todos los campos
        fields = ['balance']
        #les decimos cuales son los de solo lectura 
class PrestamoClienteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Prestamo
        #indicamos que use todos los campos
        fields = ['loan_type', 'loan_total']

class PrestamoSucursalSerializer(serializers.ModelSerializer):
     class Meta:
        model = Prestamo
        #indicamos que use todos los campos
        fields = "__all__"

class DireccionesClienteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Direcciones
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
class TipoClienteSerializer(serializers.ModelSerializer):
     class Meta:
        model = TipoCliente
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
class TipoCuentaClienteSerializer(serializers.ModelSerializer):
     class Meta:
        model = TipoCuenta
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura

class SucursalSerializer(serializers.ModelSerializer):
     class Meta:
        model = Sucursal
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 
        
class MovimientoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Movimiento
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 

class PrestamoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Prestamo
        fields = "__all__"

class EmpleadoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Empleado
        fields = "__all__"
        
class TarjetaSerializer(serializers.ModelSerializer):
       class Meta:
          model = Tarjeta
          fields = "__all__ "


class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = "__all__"