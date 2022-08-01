"""
Serializers for prispevok APIs
"""
import requests

from rest_framework import serializers

from core.models import Prispevok, User


class PrispevokSerializer(serializers.ModelSerializer):
    """Serializer for prispevok"""
    class Meta:
        model = Prispevok
        fields = ['id', 'title', 'userId']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_id = validated_data.get('userId')
        if User.objects.filter(user_id=user_id).exists():
            return Prispevok.objects.create(**validated_data)
        else:
            url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
            r = requests.get(url, headers={'Content-Type': 'application/json'})
            j_user = r.json()
            if j_user:
                # get_user_model().objects.create_user(**j_user)
                return Prispevok.objects.create(**validated_data)
            else:
                raise ValueError('User doesnt exist')

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class PrispevokDetailSerializer(PrispevokSerializer):
    """Serializer for prispevok with body"""
    class Meta(PrispevokSerializer.Meta):
        fields = PrispevokSerializer.Meta.fields + ['body']
