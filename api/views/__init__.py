from django.shortcuts import redirect
from django.shortcuts import render

from .article import ArticleViewSet
from .authorizer import AuthorizerViewSet
from .breakout import BreakoutViewSet
from .county import CountyViewSet
from .event import EventViewSet
from .publisher import PublisherViewSet


def index(request):
    return render(request, "index.html")


def go_favicon(request):
    """
    Return a favicon icon which avoids 404 Not Found errors in the access log
    """
    response = redirect("static/favicon.ico", permanent=True)
    return response
