from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Breakout


class BreakoutResource(resources.ModelResource):
    class Meta:
        model = Breakout
        fields = ("id", "as_of", "county__name", "cases", "deaths", "source__name")


class BreakoutAdmin(ImportExportModelAdmin):
    resource_class = BreakoutResource
    list_display = ["as_of", "county", "cases", "deaths"]

    list_filter = [
        "county",
    ]


admin.site.register(Breakout, BreakoutAdmin)
