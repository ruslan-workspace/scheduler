from rest_framework.permissions import BasePermission

from src.apps.events.models import Event


class IsEventsOwner(BasePermission):
    def has_object_permission(self, request, view, obj: Event):
        return obj.owner == request.user
