from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Event
        fields = ('pk','title', 'start', 'end', 'user')
        

    