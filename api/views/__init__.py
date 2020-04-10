from django.shortcuts import redirect
from django.shortcuts import render

from .article import ArticleViewSet
from .authorizer import AuthorizerViewSet
from .case import CaseViewSet
from .case_summary import CaseSummaryViewSet
from .county import CountyViewSet
from .event import EventViewSet
from .publisher import PublisherViewSet
from .screenshot import get_screenshot
from .tag import TagViewSet


def index(request):
    return render(request, "index.html")


def go_favicon(request):
    """
    Return a favicon icon which avoids 404 Not Found errors in the access log
    """
    response = redirect("static/favicon.ico", permanent=True)
    return response
