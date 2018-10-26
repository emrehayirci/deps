from rest_framework import serializers
from api.posts.models import Post, Comment, DownVote, UpVote
from datetime import datetime


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=255)
    body = serializers.CharField()
    creation_date = serializers.ReadOnlyField()
    update_date = serializers.ReadOnlyField()
    author = serializers.CreateOnlyDefault(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.update_date = datetime.now()
        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    body = serializers.CharField()
    creation_date = serializers.ReadOnlyField()
    update_date = serializers.ReadOnlyField()
    author = serializers.CreateOnlyDefault(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.update_date = datetime.now()
        instance.save()
        return instance
