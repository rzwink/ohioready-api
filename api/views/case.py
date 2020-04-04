from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_json_api import views
from rest_framework_json_api.django_filters import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Case
from api.serializers import CaseSerializer


class CaseViewSet(AutoPrefetchViewSetMixin, views.ModelViewSet):
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

    @cache_response()
    def get(self, request, *args, **kwargs):
        super(CaseViewSet, self).get(request, *args, **kwargs)
