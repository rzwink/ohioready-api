from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer
from taggit_serializer.serializers import TagListSerializerField

from api.models import Event
from api.serializers import AuthorizerSerializer


class EventSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Event

        fields = [
            "published_on",
            "scope",
            "title",
            "slug",
            "summary",
            "content",
            "authoritative_url",
            "authoritative_publisher",
            "authorizer",
            "tags",
            "article",
        ]
