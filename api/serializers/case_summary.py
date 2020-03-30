from rest_framework import serializers

from api.models import Case


class CaseSummarySerializer(serializers.HyperlinkedModelSerializer):
    county = serializers.CharField(source="county.name", read_only=True)

    class Meta:
        model = Case
        fields = ["county", "as_of", "total", "deaths", "recovered"]
