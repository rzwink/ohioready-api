from rest_framework import serializers

from api.models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
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
