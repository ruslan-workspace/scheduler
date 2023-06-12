from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.users.models import User 

class Event(TimeStampedModel):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
