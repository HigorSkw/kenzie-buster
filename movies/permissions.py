from rest_framework import permissions
from rest_framework.views import Request, View
from movies.models import Movie


class IsMovieOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, movie: Movie) -> bool:
        return movie.user == request.user


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True

        return False
