from django.db import models

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True, blank=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'


class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True)
    numero_de_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.TextField(blank=True, null=True)
    tipo_de_operacion = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'movimientos'
        verbose_name_plural = "Movimientos"

class TiposDeCuenta(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True)
    nombre_cuenta = models.TextField()

    class Meta:
        db_table = 'tipos_de_cuenta'

