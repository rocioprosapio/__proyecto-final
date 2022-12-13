from django import forms
from ejemplo.models import Familiar, Viajes, Compras


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100) #prueba

class BuscarViajes(forms.Form):
    destino = forms.CharField(max_length=100) #prueba

class BuscarCompras(forms.Form):
    descripcion = forms.CharField(max_length=100) #prueba
    
class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'direccion', 'numero_pasaporte']

class ViajesForm(forms.ModelForm):
    class Meta:
        model = Viajes
        fields = ['destino', 'transporte', 'cantidad_dias']

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['articulo', 'descripcion', 'sucursal', 'unidades']
