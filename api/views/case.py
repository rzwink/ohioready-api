from rest_framework import permissions
from rest_framework import viewsets

from api.models import Case
from api.serializers import CaseSerializer


class CaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """

    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated]
