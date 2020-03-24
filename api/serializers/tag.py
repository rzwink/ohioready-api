from rest_framework import serializers

from api.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "name",
        ]
