from rest_framework.permissions import BasePermission


class IsEventsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
