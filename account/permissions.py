from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1
class IsTechnician(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the request user is an admin or the assigned technician
        return request.user.is_staff or request.user == obj.technician
