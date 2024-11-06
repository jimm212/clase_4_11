from django.shortcuts import render
from datetime import datetime
from .models import Oferta

current_date = datetime.now()
ofertas = Oferta.objects.filter(fecha_inicio__lte=current_date, 
                                fecha_fin__gte=current_date)

# Create your views here.
def index (request):
    context = {
        'current_date': current_date,
        #'is_special_offert': False, # True o False según sea el caso
        'ofertas': ofertas
    }
    return render(request,'ofertas/index.html', context) # Renderizará la plantilla index.html

