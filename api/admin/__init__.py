from django.contrib import admin
from django.utils.safestring import mark_safe

from .article import ArticleAdmin
from .authorizer import AuthorizerAdmin
from .item import ItemAdmin
from .publisher import PublisherAdmin

admin.site.site_header = mark_safe("Ohio Ready")
admin.site.site_title = "Ohio Ready"
admin.site.index_title = "Syndication Administration"
