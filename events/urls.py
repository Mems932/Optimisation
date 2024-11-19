from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, ParticipantViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'participants', ParticipantViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 
