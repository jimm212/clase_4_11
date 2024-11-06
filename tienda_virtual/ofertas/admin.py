from django.contrib import admin
from .models import Oferta

# Register your models here.
@admin.register(Oferta)

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin')
    search_fields = ('producto__nombre', )