from django.core.validators import MinLengthValidator
from django.db import models
from django.db import models

comunas_santiago = [
    (0, "Santiago"),
    (1, "Cerrillos"),
    (2, "Cerro Navia"),
    (3, "Conchalí"),
    (4, "El Bosque"),
    (5, "Estación Central"),
    (6, "Huechuraba"),
    (7, "Independencia"),
    (8, "La Cisterna"),
    (9, "La Florida"),
    (10, "La Granja"),
    (11, "La Pintana"),
    (12, "La Reina"),
    (13, "Las Condes"),
    (14, "Lo Barnechea"),
    (15, "Lo Espejo"),
    (16, "Lo Prado"),
    (17, "Macul"),
    (18, "Maipú"),
    (19, "Ñuñoa"),
    (20, "Providencia"),
    (21, "Quilicura"),
    (22, "Quinta Normal"),
    (23, "Recoleta"),
    (24, "Renca"),
    (25, "San Joaquín"),
    (26, "San Miguel"),
    (27, "San Ramón"),
    (28, "Vitacura"),
]

motivo = [
    (0, "Objetos Faltantes/Inexistentes"),
    (1, "Pedido comprado por error"),
    (2, "Cambio/Devolución"),
    (3, "Otro")
]

talla_choices = [
    (0, "S"),
    (1, "M"),
    (2, "L"),
    (3, "XL"),
]

class Genero(models.Model):
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.genero

class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='idGenero', default=1) 
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

    class Meta:
        ordering = ['rut']


class Devolucion(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    motivo = models.IntegerField(choices=motivo)
    mensaje = models.TextField(blank=True, null=True)
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Pagar(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20, default='')
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=20)
    comuna = models.IntegerField(choices=comunas_santiago)

    def __str__(self):
        return self.nombre

class Login(models.Model):
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=200, validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.usuario

class Register(models.Model):
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=200, validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.usuario

class AgregarProductos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    talla = models.IntegerField(choices=talla_choices) 
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='files/', blank=True, null=True)


    def __str__(self):
        return f"{self.id} - {self.nombre}"
    
    def get_talla_display(self):
        return dict(talla_choices).get(self.talla, "Desconocido")