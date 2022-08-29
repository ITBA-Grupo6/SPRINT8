from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def clientes(request):
    if request.user.username:
        return render(request, "Clientes/clientes.html", {'name': request.user.username})
    else: 
        return render(request, "Clientes/clientes.html")
