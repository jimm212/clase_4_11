from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Crea grupos y usuarios de prueba! para las aplicaciones y asigna permisos'

    def asignar_permisos_grupos(self, grupo_nombre, permisos):
        grupo , creado = Group.objects.get_or_create(name=grupo_nombre)
        
        for permiso in permisos:
            grupo.permissions.add(Permission.objects.get(codename=permiso))
    
    #def handle():
        