from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin
from import_export import fields
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget

from api.models import Authorizer
from api.models import Event
from api.models import Tag


class EventResource(resources.ModelResource):
    authorizer = fields.Field(
        column_name="authorizer",
        attribute="authorizer",
        widget=ForeignKeyWidget(Authorizer, "name"),
    )
    tags = fields.Field(
        column_name="tags",
        attribute="tags",
        widget=ManyToManyWidget(Tag, field="name", separator="|"),
    )

    class Meta:
        model = Event
        fields = (
            "id",
            "published_on",
            "tags",
            "scope",
            "authorizer",
            "title",
            "authoritative_url",
        )
        export_order = (
            "id",
            "published_on",
            "tags",
            "scope",
            "authorizer",
            "title",
            "authoritative_url",
        )
        skip_unchanged = True


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
    ]

    def article_display(self, obj):
        return ", ".join([article.publisher.name for article in obj.article.all()])

    article_display.short_description = "Article"


admin.site.register(Event, EventAdmin)
