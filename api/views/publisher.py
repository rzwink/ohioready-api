from rest_framework import permissions
from rest_framework import viewsets

from api.models import Publisher
from api.serializers import PublisherSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Publisher.objects.all().order_by("-created_on")
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]
