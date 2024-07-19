from django import forms
from .models import Devolucion,Pagar,AgregarProductos

class devolucionForm(forms.ModelForm):
    class Meta:
        model = Devolucion
        fields = '__all__'  # Para incluir todos los campos del modelo Devolucion


class PagarForm(forms.ModelForm):
    class Meta:
        model = Pagar
        fields = '__all__'



class AgregarProductosForm(forms.ModelForm):
    class Meta:
        model = AgregarProductos
        fields = ['nombre','precio', 'descripcion', 'talla', 'imagen']
