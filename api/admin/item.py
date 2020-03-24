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
        "article_display",
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

    def article_display(self, obj):
        return ", ".join([article.publisher.name for article in obj.article.all()])

    article_display.short_description = "Article"


admin.site.register(Item, ItemAdmin)
