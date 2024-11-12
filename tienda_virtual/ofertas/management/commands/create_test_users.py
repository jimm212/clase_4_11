from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Crea grupos y usuarios de prueba! para las aplicaciones y asigna permisos'

    def asignar_permisos_grupos(self, grupo_nombre, permisos):
        grupo , creado = Group.objects.get_or_create(name=grupo_nombre)
        
        for permiso in permisos:
            grupo.permissions.add(Permission.objects.get(codename=permiso))
    
    def handle(self, *args, **kwargs):
        # Verificando y creando (si no existe) el usuario admin
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults = {'email': 'admin@admin.cl', 'is_staff': True}
            )
        #
        if created: 
            admin_user.set_password('adminpass')
            admin_user.is_active = True
            admin_user.save()
        
        # Verificando y creando (si no existe) el usuario editor
        editor_user, created = User.objects.get_or_create(
            username='editor',
            defaults = {'email': 'editor@editor.cl'}
            )
        #
        if created: 
            editor_user.set_password('editorpass')
            editor_user.is_active = True
            editor_user.save()
            
        # Verificando y creando (si no existe) el usuario invitado
        guest_user, created = User.objects.get_or_create(
            username='guest',
            defaults = {'email': 'guest@guest.cl'}
            )
        #
        if created: 
            guest_user.set_password('guestpass')
            guest_user.is_active = True
            guest_user.save()
        
        # Asignando permisos a los grupos
        self.asignar_permisos_grupos('Admin' , ['add_oferta', 'delete_oferta', 'change_oferta', 'view_oferta'])
        self.asignar_permisos_grupos('Editor', ['add_oferta','view_oferta'])
        self.asignar_permisos_grupos('Guest' , ['view_oferta'])
        
        try:
            admin_group  = Group.objects.get(name='Admin')
            editor_group = Group.objects.get(name='Editor')
            guest_group  = Group.objects.get(name='Guest')
            
            admin_user.groups.add(admin_group)
            editor_user.groups.add(editor_group)
            guest_user.groups.add(guest_group)
            
        except Group.DoesNotExist:
            self.stdout.write(self.style.WARNING("Los grupos no existen. Asegúrate de que los grupos 'Admin', 'Editor' y 'Guest' existan."))
        
        self.stdout.write(self.style.SUCCESS("Usuarios y permisos creados exitosamente."))
        