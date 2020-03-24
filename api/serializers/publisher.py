from rest_framework import serializers

from api.models import Item
from api.models import Publisher


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = [
            "name",
            "homepage_url",
            "type",
            "phone",
            "email",
        ]
