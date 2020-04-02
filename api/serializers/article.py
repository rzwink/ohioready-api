from rest_framework import serializers

from api.models import Article
from api.models import Event
from api.models import Publisher


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        "publisher": "api.serializers.PublisherSerializer",
    }

    class Meta:
        model = Article
        fields = [
            "url",
            "publisher",
            "event",
            "media_type",
            "created_on",
        ]
