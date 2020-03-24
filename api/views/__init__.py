from django.shortcuts import redirect
from django.shortcuts import render

from .authorizer import AuthorizerViewSet
from .coverage import CoverageViewSet
from .item import ItemViewSet
from .publisher import PublisherViewSet


def index(request):
    return render(request, "index.html")


def go_favicon(request):
    """
    Return a favicon icon which avoids 404 Not Found errors in the access log
    """
    response = redirect("static/favicon.ico", permanent=True)
    return response
