from rest_framework import permissions

from makeup.models import MakeUpArtist


class IsMakeUpArtist(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and isinstance(request.user, MakeUpArtist))
