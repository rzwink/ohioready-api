import urllib

from django.contrib import admin
from django.utils.html import format_html
from fsm_admin.mixins import FSMTransitionMixin
from import_export import fields
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget

from api.models import Article
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
            "media_type",
        )
        export_order = (
            "id",
            "published_on",
            "tags",
            "scope",
            "authorizer",
            "title",
            "authoritative_url",
            "media_type",
        )
        skip_unchanged = True


def publish(modeladmin, request, queryset):
    for event in queryset:
        event.publish()
        event.save()


def clean_url(modeladmin, request, queryset):
    for event in queryset:
        event.authoritative_url = urllib.parse.splitquery(event.authoritative_url)[0]
        event.save()


class ArticleInline(admin.TabularInline):
    model = Article


class EventAdmin(FSMTransitionMixin, ImportExportModelAdmin):
    inlines = [
        ArticleInline,
    ]

    resource_class = EventResource
    autocomplete_fields = ["tags"]
    actions = [publish, clean_url]
    list_display = [
        "published_on",
        "status",
        "scope",
        "authorizer",
        "title",
        "_authoritative_url",
        "authorizer",
        "article_display",
        "media_type",
    ]
    list_filter = ["scope", "authorizer", "status"]
    search_fields = [
        "title",
        "summary",
        "content",
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

    def _authoritative_url(self, obj):
        color = "purple"
        if len(obj.authoritative_url) == 0:
            color = "red"
        return format_html(
            u'<a href="{}"><i class="fas fa-file" style="color: {}" title="Click to view URL"></i></a>',
            obj.authoritative_url,
            color,
        )

    article_display.short_description = "Article"


admin.site.register(Event, EventAdmin)
