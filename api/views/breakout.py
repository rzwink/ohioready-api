from rest_framework import permissions
from rest_framework import viewsets

from api.models import Breakout
from api.models import County
from api.serializers import BreakoutSerializer
from api.serializers import CountySerializer


class BreakoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """

    queryset = Breakout.objects.all()
    serializer_class = BreakoutSerializer
    permission_classes = [permissions.IsAuthenticated]
