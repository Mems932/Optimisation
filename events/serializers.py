from rest_framework import serializers
from .models import Event, Participant


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' # Séléctionne les champs renvoyés (serializés)


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'