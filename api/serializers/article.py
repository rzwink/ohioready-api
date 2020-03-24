from rest_framework import serializers

from api.models import Article
from api.models import Item
from api.models import Publisher


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = [
            "url",
            "publisher",
            "item",
            "created_on",
        ]
