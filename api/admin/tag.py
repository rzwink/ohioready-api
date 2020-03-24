from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Tag


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource
    list_display = [
        "name",
    ]
    search_fields = ["name"]


admin.site.register(Tag, TagAdmin)
