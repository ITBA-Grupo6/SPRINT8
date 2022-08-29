from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Cuentas.models import Cuenta

@login_required
# Create your views here.
def cuentas(request):
    iban = request.user.username
    cuenta = Cuenta.objects.get(iban = iban)
    saldo = int(cuenta.balance)  
    return render(request, "Cuentas/cuentas.html", {'saldo': saldo})
    