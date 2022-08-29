from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreatePrestamo
from .models import Prestamo
from Cuentas.models import Cuenta
@login_required
def prestamos(request):
    form = CreatePrestamo
    
    if request.method == 'POST':        
        form = form(data=request.POST)
        
        if form.is_valid():
            estado = 0            
            customer_id = 255            
            iban = request.user.username
            tipoCuenta = request.POST.get('cuenta', '')
            tipoPrestamo = request.POST['tipo'].upper(),
            monto = request.POST['monto']
            fecha = '{}-{}-{}'.format(request.POST['fecha_year'], request.POST['fecha_month'], request.POST['fecha_day'])

            
            if tipoCuenta == 'CLASSIC':
                if int(monto) <= 100000: 
                    prestamo = Prestamo(loan_type=tipoPrestamo, loan_date=fecha,
                                loan_total=monto, customer_id=customer_id)
                    prestamo.save()  
                    cuenta = Cuenta.objects.get(iban = iban)                    
                    cuenta.balance += int(monto)
                    cuenta.save()                  
                    estado = 1
                if int(monto) > 100000:
                    estado = 2
            if tipoCuenta == 'GOLD':
                if int(monto) <= 300000: 
                    prestamo = Prestamo(loan_type=tipoPrestamo, loan_date=fecha,
                                loan_total=monto, customer_id=customer_id)
                    prestamo.save()
                    cuenta = Cuenta.objects.get(iban = iban)                    
                    cuenta.balance += int(monto)
                    cuenta.save()
                    estado = 1
                else:
                    prestamo = Prestamo(loan_type=tipoPrestamo, loan_date=fecha,
                                loan_total=monto, customer_id=customer_id)
                    prestamo.save()
                    cuenta = Cuenta.objects.get(iban = iban)                    
                    cuenta.balance += int(monto)
                    cuenta.save()
                    estado = 2
            if tipoCuenta == 'BLACK':
                if int(monto) <= 500000: 
                    prestamo = Prestamo(loan_type=tipoPrestamo, loan_date=fecha,
                                loan_total=monto, customer_id=customer_id)
                    prestamo.save()
                    cuenta = Cuenta.objects.get(iban = iban)                    
                    cuenta.balance += int(monto)
                    cuenta.save()
                    estado = 1
                else:
                    prestamo = Prestamo(loan_type=tipoPrestamo, loan_date=fecha,
                                loan_total=monto, customer_id=customer_id)
                    prestamo.save()
                    estado = 2     
            return render(request, 'Prestamos/prestamos.html', {'estado': estado})     
    return render(request, 'Prestamos/prestamos.html', {'form': form})




