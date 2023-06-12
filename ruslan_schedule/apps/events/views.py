from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializers import EventSerializer
from .permissions import IsEventsOwner


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, IsEventsOwner)

    def get_queryset(self):
        self.queryset = self.queryset.filter(user=self.request.user.username)
        return super().get_queryset()
