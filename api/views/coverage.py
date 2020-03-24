from rest_framework import permissions
from rest_framework import viewsets

from api.models import Coverage
from api.serializers import CoverageSerializer


class CoverageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows coverage to be viewed or edited.
    """

    queryset = Coverage.objects.all().order_by("-created_on")
    serializer_class = CoverageSerializer
    permission_classes = [permissions.IsAuthenticated]
