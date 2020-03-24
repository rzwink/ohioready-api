from django.contrib import admin
from django.utils.safestring import mark_safe

from .item import ItemAdmin

admin.site.site_header = mark_safe("Ohio Ready")
admin.site.site_title = "Ohio Ready"
admin.site.index_title = "Syndication Administration"
