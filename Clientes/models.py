from django.db import models

# Create your models here.
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True, blank=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'
        

class TiposDeCliente(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True)
    nombre_tipo = models.TextField()
    tarjetas_de_debito = models.TextField(blank=True, null=True)  
    caja_de_ahorro_usd = models.TextField()
    descubierto = models.IntegerField()
    tarjetas_de_credito = models.IntegerField()
    retiro_de_efectivo = models.IntegerField()
    chequeras = models.IntegerField()
    comision_por_transferencia = models.DecimalField(max_digits = 5, decimal_places = 2)
    max_transferencias = models.IntegerField(blank=True, null=True)
    max_prestamo = models.IntegerField(null=True, blank = True)

    class Meta:
        managed = False
        db_table = 'tipos_de_cliente'
    
    def __str__(self):
        return self.nombre_tipo