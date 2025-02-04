from django.db import models
from .choices import CARGO
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, MaxLengthValidator
from .validadores import validacion_numeros
# Create your models here.

class Empleados (models.Model):
    Cedual = models.CharField(max_length=10, primary_key=True, min_length=10, v)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    cargo = models.CharField(max_length=50,choices=CARGO,)

    class Meta:
        verbose_name_plural = 'Empleados xx'
        verbose_name = 'Empleado yy'
        bd_table = 'Empleado'

    def __str__(self):
        return self.Nombre +" " + self.Apellido
    
