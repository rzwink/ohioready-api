from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Authorizer


class AuthorizerResource(resources.ModelResource):
    class Meta:
        model = Authorizer
        exclude = (
            "created_on",
            "status",
        )


class AuthorizerAdmin(ImportExportModelAdmin):
    resource_class = AuthorizerResource
    list_display = [
        "name",
    ]


admin.site.register(Authorizer, AuthorizerAdmin)
