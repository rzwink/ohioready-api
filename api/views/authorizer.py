from rest_framework import permissions
from rest_framework import viewsets

from api.models import Authorizer
from api.serializers import AuthorizerSerializer


class AuthorizerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Authorizer.objects.all().order_by("-created_on")
    serializer_class = AuthorizerSerializer
    permission_classes = [permissions.IsAuthenticated]
