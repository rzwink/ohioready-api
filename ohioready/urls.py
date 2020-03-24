"""ohioready URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from api import views

router = routers.DefaultRouter()
router.register(r"event", views.EventViewSet)
router.register(r"publisher", views.PublisherViewSet)
router.register(r"authorizer", views.AuthorizerViewSet)
router.register(r"article", views.ArticleViewSet)

router.register(r"county", views.CountyViewSet)
router.register(r"breakout", views.BreakoutViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("admin/", admin.site.urls),
    url(r"^api-auth/", include("rest_framework.urls")),
    path("", views.index, name="homepage"),
    url(r"^favicon.ico", views.go_favicon, name="favicon"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
