from rest_framework import serializers

from api.models import Authorizer


class AuthorizerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Authorizer
        fields = [
            "name",
        ]
