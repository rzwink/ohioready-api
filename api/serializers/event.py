from rest_framework import serializers

from api.models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        "authorizer": "api.serializers.AuthorizerSerializer",
        "tags": "api.serializers.TagSerializer",
        "article": "api.serializers.ArticleSerializer",
    }

    class Meta:
        model = Event
        fields = [
            "published_on",
            "scope",
            "title",
            "summary",
            "content",
            "authoritative_url",
            "authorizer",
            "tags",
            "article",
            "media_type",
        ]
