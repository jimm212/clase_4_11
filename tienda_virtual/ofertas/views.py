from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'ofertas/index.html') # Renderizará la plantilla index.html

