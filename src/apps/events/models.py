from django.db import models
from django_extensions.db.models import TimeStampedModel

from src.apps.users.models import User


class Event(TimeStampedModel):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_events"
    )
    description = models.TextField(blank=True)
    meeting_link = models.URLField(blank=True, null=True)
