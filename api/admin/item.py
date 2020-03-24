from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Item


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        exclude = ("created_on",)


class ItemAdmin(FSMTransitionMixin, ImportExportModelAdmin):
    resource_class = ItemResource
    list_display = [
        "published_on",
        "impact_area",
        "authorizer",
        "title",
        "status",
        "authorizer",
    ]
    list_filter = ["impact_area", "authorizer", "status"]
    search_fields = [
        "title",
        "summary",
        "content",
        "authoritative_publisher",
        "authorizer",
    ]
    fsm_field = [
        "status",
    ]

    readonly_fields = [
        "status",
        "slug",
    ]


admin.site.register(Item, ItemAdmin)
