from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Case


class CaseResource(resources.ModelResource):
    class Meta:
        model = Case
        fields = (
            "id",
            "as_of",
            "county__name",
            "total",
            "deaths",
        )


class CaseAdmin(ImportExportModelAdmin):
    resource_class = CaseResource
    list_display = ["as_of", "county", "total", "deaths"]

    list_filter = [
        "county",
    ]


admin.site.register(Case, CaseAdmin)
