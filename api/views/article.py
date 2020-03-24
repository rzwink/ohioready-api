from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Article
from api.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """

    queryset = Article.objects.all().order_by("-created_on")
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (
        TokenAuthentication,
        SessionAuthentication,
        JWTAuthentication,
    )
