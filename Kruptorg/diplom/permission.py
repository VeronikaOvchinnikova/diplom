from rest_framework.permissions import BasePermission


class IsStorekeeper(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Кладовщик').exists()

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Менеджер').exists()

