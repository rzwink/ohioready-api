from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Authorizer
from api.serializers import AuthorizerSerializer


class AuthorizerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authorizers to be viewed or edited.
    """

    queryset = Authorizer.objects.all().order_by("-created_on")
    serializer_class = AuthorizerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (
        TokenAuthentication,
        SessionAuthentication,
        JWTAuthentication,
    )
