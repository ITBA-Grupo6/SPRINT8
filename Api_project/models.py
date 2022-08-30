from django.db import models

class Cliente(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'

class Direcciones(models.Model):
    direccion_id = models.IntegerField(primary_key=True)
    calle = models.TextField()
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    direccion_empleado_id = models.IntegerField(blank=True, null=True)
    direccion_cliente_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'



class Cuenta(models.Model):
    account_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'

class Empleado(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'

class Movimiento(models.Model):
    movimiento = models.IntegerField(primary_key=True)
    numerocuenta = models.IntegerField(db_column='numeroCuenta')  # Field name made lowercase.
    monto = models.IntegerField()
    tipooperacion = models.IntegerField(db_column='tipoOperacion')  # Field name made lowercase.
    hora = models.TimeField()

    class Meta:
        managed = False
        db_table = 'movimientos'

class Sucursal(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'

class Prestamo(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'

class TipoCliente(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    description_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

class TipoCuenta(models.Model):
    tipo_id = models.IntegerField(primary_key=True)
    descripcion_cuenta = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'

class ids(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente_id = models.IntegerField(blank=True, null=False)
    username = models.TextField(blank=True, null=False)
    tipo = models.TextField(blank=True, null=False)
    class Meta:            
        db_table = 'ids'


class MarcaTarjeta(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_brand = models.ForeignKey(
        MarcaTarjeta, models.DO_NOTHING, db_column='card_brand')
    card_number = models.TextField(unique=True)
    card_cvv = models.IntegerField()
    card_from_date = models.DateTimeField()
    card_expiration_date = models.DateTimeField()
    card_type = models.TextField()
    card_customer = models.ForeignKey(
        Cliente, models.DO_NOTHING, db_column='card_customer')

    class Meta:
        managed = False
        db_table = 'tarjeta'

