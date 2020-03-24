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
    search_fields = [
        "title",
        "summary",
        "content",
        "press_release_publisher",
        "authorizer",
    ]
    fsm_field = [
        "status",
    ]


admin.site.register(Item, ItemAdmin)
