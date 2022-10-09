"""User permissions"""

# Django Rest framework
from rest_framework.permissions import BasePermission

class IsAccountOwner(BasePermission):
    """Only can access if belongs to user"""
    message = 'No tiene permiso para acceder a este recurso'
    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj
