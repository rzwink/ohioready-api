from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Publisher
from api.serializers import PublisherSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows publishers to be viewed or edited.
    """

    queryset = Publisher.objects.all().order_by("-created_on")
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (
        TokenAuthentication,
        SessionAuthentication,
        JWTAuthentication,
    )
