from rest_framework import serializers
from .models import Event, Participant


class EventSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__' # Séléctionne les champs renvoyés (serializés)


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

    def validate(self, data):
        event = data.get('event')
        if event.participants.all().count() >= event.max_participants:
            raise serializers.ValidationError("Maximum de personnes atteint.")
        return data