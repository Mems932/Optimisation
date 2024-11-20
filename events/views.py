from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import EventSerializer, ParticipantSerializer
from .models import Event, Participant
from rest_framework.permissions import IsAuthenticated

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'location']
    ordering_fields = ['date', 'max_participants']
    permission_classes = [IsAuthenticated]


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]
# Create your views here.
