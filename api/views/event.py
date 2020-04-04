from django_auto_prefetching import AutoPrefetchViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Event
from api.serializers import EventSerializer


class EventViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """

    queryset = Event.objects.filter(status="published").order_by("-published_on")
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (
        TokenAuthentication,
        SessionAuthentication,
        JWTAuthentication,
    )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "scope",
        "tags",
        "authorizer__name",
        "media_type",
    ]
    search_fields = ["summary", "content", "title"]

    @cache_response()
    def get(self, request, *args, **kwargs):
        super(EventViewSet, self).get(request, *args, **kwargs)
