from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Event


class EventResource(resources.ModelResource):
    class Meta:
        model = Event
        exclude = ("created_on",)


class EventAdmin(FSMTransitionMixin, ImportExportModelAdmin):
    resource_class = EventResource
    autocomplete_fields = ["tags"]

    list_display = [
        "published_on",
        "scope",
        "authorizer",
        "title",
        "status",
        "authorizer",
        "article_display",
    ]
    list_filter = ["scope", "authorizer", "status"]
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


admin.site.register(Event, EventAdmin)
