from django.db import models

# Create your models here.

class MarcaTarjeta(models.Model):
    marca_id = models.TextField(primary_key=True)
    nombre_tarjeta = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'

class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    numero = models.TextField(unique=True)
    cvv = models.IntegerField()
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo = models.TextField()
    tarjeta_marca = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING, blank=True, null=True)
    tarjeta_cliente_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjeta'

