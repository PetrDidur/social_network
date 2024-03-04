from rest_framework import serializers

from social_network.models import Post, Comment
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

from social_network.validators import AgeValidator, ForbiddenWordsValidator
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        validators = [AgeValidator(field='author'),
                      ForbiddenWordsValidator(field='header')
                      ]

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
