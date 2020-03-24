from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer
from taggit_serializer.serializers import TagListSerializerField

from api.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Item
        fields = [
            "published_on",
            "impact_area",
            "title",
            "slug",
            "summary",
            "content",
            "authoritative_url",
            "authoritative_publisher",
            "authorizer",
            "tags",
            "coverage",
        ]
