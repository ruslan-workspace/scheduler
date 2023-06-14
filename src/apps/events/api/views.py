from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.apps.events.models import Event
from .serializers import EventSerializer
from .permissions import IsEventsOwner


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, IsEventsOwner)

    def get_queryset(self) -> QuerySet[Event]:
        self.queryset = super().get_queryset()
        if self.action == "list":
            self.queryset = self.queryset.filter(user=self.request.user.username)
        return self.queryset
