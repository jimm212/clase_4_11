from django.shortcuts import redirect, render
from datetime import datetime
from .models import Oferta
from django.http import Http404
from .forms import OfertaForm


# Create your views here.
def crear_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ofertas:index')
    else:
        form = OfertaForm()
    return render(request, 'ofertas/crear_oferta.html', {'form': form})


def index (request):
    current_date = datetime.now()
    ofertas = []
    
    try:
        ofertas = Oferta.objects.filter(fecha_inicio__lte=current_date, 
                                    fecha_fin__gte=current_date)
        # raise Exception('Error Inesperado')
    
        if not ofertas:
            raise ValueError("No hay ofertas disponibles en este momento.")
    except ValueError as e:
        # Manejar el error especifico ValueError
        return render(request, 'ofertas/index.html', {'error': str(e), 'current_date': current_date})
    except Exception as e:
        # Manejar cualquier otro error
        return render(request, 'ofertas/index.html', {'error': 'Se produjo un error inesperado!','current_date': current_date})
            
    context = {
        'current_date': current_date,
        #'is_special_offert': False, # True o False según sea el caso
        'ofertas': ofertas
    }
    return render(request,'ofertas/index.html', context) # Renderizará la plantilla index.html
    
