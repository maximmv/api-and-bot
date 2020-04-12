from abc import ABC

from rest_framework import serializers
from .models import Post, Like
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        post = Post.objects.all().filter(author=instance).only('created')
        like = Like.objects.all().filter(author=instance).only('created')
        last_active = post.union(like).order_by('-created').first()
        ret = super().to_representation(instance)

        ret['last_activity'] = getattr(last_active, 'created') if last_active else None
        return ret

    class Meta:
        model = User
        fields = ('id', 'username', 'last_login')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('author', 'created',)

    def validate(self, data):
        data = super().validate(data)
        request = self.context['request']
        data['author'] = request.user
        return data


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'created', )
        read_only_fields = ('author', 'created',)

    def validate(self, data):
        data = super().validate(data)
        request = self.context['request']
        data['author'] = request.user
        return data


class AnalyticSerializer(serializers.Serializer):
    date = serializers.DateField()
    liked = serializers.IntegerField()
    disliked = serializers.IntegerField()
