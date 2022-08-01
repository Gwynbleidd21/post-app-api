"""
Serializers for prispevok APIs
"""
from rest_framework import serializers

from core.models import Prispevok
import requests


class PrispevokSerializer(serializers.ModelSerializer):
    """Serializer for prispevok"""
    class Meta:
        model = Prispevok
        fields = ['id', 'title', 'userId']
        read_only_fields = ['id', 'userId']


class PrispevokDetailSerializer(PrispevokSerializer):
    """Serializer for prispevok with body"""
    class Meta(PrispevokSerializer.Meta):
        fields = PrispevokSerializer.Meta.fields + ['body']


