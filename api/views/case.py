from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_json_api.django_filters import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Case
from api.serializers import CaseSerializer


class CaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """

    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (
        TokenAuthentication,
        SessionAuthentication,
        JWTAuthentication,
    )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "county__name",
        "as_of",
    ]
