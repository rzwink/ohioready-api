from rest_framework import serializers

from api.models import Breakout


class BreakoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breakout
        fields = [
            "county",
            "as_of",
            "cases",
            "deaths",
            "source",
        ]
