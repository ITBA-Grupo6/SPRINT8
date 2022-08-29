from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def tarjetas(request):
    if request.user.username:
        return render(request, "Tarjetas/tarjetas.html", {'name': request.user.username})
    else: 
        return render(request, "Tarjetas/tarjetas.html")