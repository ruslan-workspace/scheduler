from django.db import models
from django_extensions.db.models import TimeStampedModel


class Event(TimeStampedModel):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="created_events"
    )
    description = models.TextField(blank=True)
    meeting_link = models.URLField(blank=True, null=True)
    guests = models.ManyToManyField("users.User", through="invitations.Invitation")
