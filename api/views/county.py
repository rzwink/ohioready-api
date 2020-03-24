from rest_framework import permissions
from rest_framework import viewsets

from api.models import County
from api.serializers import CountySerializer


class CountyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """

    queryset = County.objects.all().order_by("name")
    serializer_class = CountySerializer
    permission_classes = [permissions.IsAuthenticated]
