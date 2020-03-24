from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Publisher


class PublisherResource(resources.ModelResource):
    class Meta:
        model = Publisher
        exclude = ("created_on",)


class PublisherAdmin(ImportExportModelAdmin):
    resource_class = PublisherResource
    list_display = [
        "name",
        "type",
        "phone",
        "email",
    ]


admin.site.register(Publisher, PublisherAdmin)
