from django.urls import path
from . import views

app_name = 'ofertas'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_oferta/', views.crear_oferta, name='crear_oferta')
]
