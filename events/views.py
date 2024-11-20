from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import EventSerializer, ParticipantSerializer
from .models import Event, Participant


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'location']


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
# Create your views here.
