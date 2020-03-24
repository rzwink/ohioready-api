from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import County


class CountyResource(resources.ModelResource):
    class Meta:
        model = County
        exclude = ("created_on",)


class CountyAdmin(ImportExportModelAdmin):
    resource_class = CountyResource
    list_display = [
        "name",
    ]


admin.site.register(County, CountyAdmin)
