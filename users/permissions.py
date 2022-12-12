from rest_framework import permissions
from .models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True

        return False


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:

        if request.user.is_employee:
            return True

        if obj == request.user:
            return True
