from drf_aggregates.exceptions import AggregateException
from drf_aggregates.renderers import AggregateRenderer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework_json_api.django_filters import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Case
from api.serializers.case_summary import CaseSummarySerializer


class CaseSummaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """

    renderer_classes = [
        AggregateRenderer,
    ]
    queryset = Case.objects.all()
    serializer_class = CaseSummarySerializer
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

    def list(self, request, *args, **kwargs):
        renderer = request.accepted_renderer
        if isinstance(renderer, AggregateRenderer):
            queryset = self.filter_queryset(self.get_queryset())
            try:
                data = request.accepted_renderer.render(
                    {"queryset": queryset, "request": request}
                )
            except AggregateException as e:
                # Raise other types of aggregate errors
                return Response(str(e), status=400)
            return Response(data, content_type=f"application/json")
        return super().list(request, *args, **kwargs)
