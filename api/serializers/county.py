from rest_framework import serializers

from api.models import County


class CountySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = County
        fields = [
            "name",
        ]
