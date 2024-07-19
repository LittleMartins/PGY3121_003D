from django.contrib import admin
from .models import Genero, Alumno, Devolucion, Pagar, Login, Register, AgregarProductos

@admin.register(Genero, Alumno, Devolucion, Pagar, Login, Register, AgregarProductos)
class Admin(admin.ModelAdmin):
    pass
