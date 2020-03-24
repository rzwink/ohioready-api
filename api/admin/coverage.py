from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Coverage


class CoverageResource(resources.ModelResource):
    class Meta:
        model = Coverage
        exclude = ("created_on",)


class CoverageAdmin(ImportExportModelAdmin):
    resource_class = CoverageResource
    list_display = ["item", "publisher", "url"]

    list_filter = [
        "publisher",
    ]


admin.site.register(Coverage, CoverageAdmin)
