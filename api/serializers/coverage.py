from rest_framework import serializers

from api.models import Coverage
from api.models import Item
from api.models import Publisher


class CoverageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coverage
        fields = [
            "url",
            "publisher",
            "item",
            "created_on",
        ]
