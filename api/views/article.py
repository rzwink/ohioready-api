from rest_framework import permissions
from rest_framework import viewsets

from api.models import Article
from api.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows article to be viewed or edited.
    """

    queryset = Article.objects.all().order_by("-created_on")
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
