from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import Article


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article
        exclude = ("created_on",)


class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource
    list_display = [
        "formatted_event_title",
        "publisher",
        "url",
        "media_type",
    ]

    list_filter = ["publisher", "media_type"]


admin.site.register(Article, ArticleAdmin)
