from rest_framework import permissions
from rest_framework import viewsets

from api.models import Event
from api.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """

    queryset = Event.objects.filter(status="published").order_by("-published_on")
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
