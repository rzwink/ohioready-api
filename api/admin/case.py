from django.contrib import admin
from import_export import fields
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from api.models import Case
from api.models import County


class CaseResource(resources.ModelResource):
    county = fields.Field(
        column_name="county",
        attribute="county",
        widget=ForeignKeyWidget(County, "name"),
    )

    class Meta:
        model = Case
        skip_unchanged = True
        import_id_fields = ("county", "as_of")
        fields = ("as_of", "county", "total", "deaths", "recovered", "county_id")
        export_order = (
            "as_of",
            "county",
            "total",
            "deaths",
            "recovered",
        )


class CaseAdmin(ImportExportModelAdmin):
    resource_class = CaseResource
    list_display = ["as_of", "county", "total", "deaths", "recovered"]

    list_filter = ["county", "as_of"]


admin.site.register(Case, CaseAdmin)
