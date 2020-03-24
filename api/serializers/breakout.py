from rest_framework import serializers

from api.models import Breakout


class BreakoutSerializer(serializers.HyperlinkedModelSerializer):
    county = serializers.CharField(source="county.name", read_only=True)
    source = serializers.CharField(source="source.name", read_only=True)

    class Meta:
        model = Breakout
        fields = [
            "county",
            "as_of",
            "cases",
            "deaths",
            "source",
        ]
