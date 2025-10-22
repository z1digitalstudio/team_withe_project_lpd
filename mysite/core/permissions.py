from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo a los propietarios de un objeto editarlo.
    """
    def has_object_permission(self, request, view, obj):
        # Permisos de lectura para cualquier request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permisos de escritura solo para el propietario del objeto
        return obj.blog.user == request.user

class IsOwnerOrSuperuser(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo al propietario o superusuario gestionar el objeto.
    """
    def has_object_permission(self, request, view, obj):
        # Superusuarios pueden hacer todo
        if request.user.is_superuser:
            return True
        
        # Solo el propietario puede gestionar su objeto
        return obj.blog.user == request.user

class IsOwnerOrSuperuserForBlog(permissions.BasePermission):
    """
    Permiso personalizado para blogs.
    """
    def has_object_permission(self, request, view, obj):
        # Superusuarios pueden hacer todo
        if request.user.is_superuser:
            return True
        
        # Solo el propietario puede gestionar su blog
        return obj.user == request.user