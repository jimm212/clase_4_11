from django.db import models
from productos.models import Productos

# Create your models here.
class Oferta(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    
    def __str__(self):
        return f" oferta en: {self.producto.nombre} --- Descuento: {self.porcentaje_descuento}%"
    
    @property
    def precio_descuento(self):
        return self.producto.precio * (1 - self.porcentaje_descuento/100)