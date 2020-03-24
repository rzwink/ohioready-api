from rest_framework import permissions
from rest_framework import viewsets

from api.models import County
from api.models import Tag
from api.serializers import CountySerializer
from api.serializers.tag import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """

    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
