from rest_framework import serializers

from api.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = [
            "title",
            "slug",
            "summary",
            "content",
            "authoritative_url",
        ]
