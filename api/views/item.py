from rest_framework import permissions
from rest_framework import viewsets

from api.models import Item
from api.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Item.objects.all().order_by("-published_on")
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]