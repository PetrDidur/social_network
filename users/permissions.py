from rest_framework.permissions import BasePermission

from users.models import User


class IsOwner(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class IsSelf(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False

class IsStaff(BasePermission):
    message = 'You must be staff.'

    def has_permission(self, request, view):
        return request.user.is_staff



