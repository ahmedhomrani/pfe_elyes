from rest_framework import permissions

class IsTechnician(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a technician
        return request.user.role == 2
