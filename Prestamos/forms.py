
from django import forms
from .models import Prestamo
tipoPrestamo = [('HIPOTECARIO', 'HIPOTECARIO'),('PERSONAL', 'PERSONAL'),('PRENDATARIO', 'PRENDATARIO')]
tipoCuenta = [('CLASSIC', 'CLASSIC'),('GOLD', 'GOLD'),('BLACK', 'BLACK')]

class CreatePrestamo(forms.Form):
    cuenta = forms.ChoiceField(label='Tipo de prestamo', choices = tipoCuenta, required=True)    
    tipo = forms.ChoiceField(label='Tipo de prestamo', choices = tipoPrestamo, required=True)
    monto = forms.IntegerField(label='Monto', min_value=1, required=True, widget=forms.NumberInput(attrs={'placeholder' : 'Ingrese el monto del prestamo', 'class' : 'form-control'}))
    fecha = forms.DateField(label='Fecha de inicio', widget=forms.SelectDateWidget, required=True)
    

    class Meta:
        model: Prestamo
        fields = '__all__'

