from rest_framework import serializers
from api.posts.models import Post, Comment, DownVote, UpVote
from datetime import datetime


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    body = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), read_only=False)
    creation_date = serializers.ReadOnlyField()
    update_date = serializers.ReadOnlyField()
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'body', 'post', 'creation_date', 'update_date', 'author')


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=255)
    body = serializers.CharField()
    comment = CommentSerializer(read_only=True, many=True)
    creation_date = serializers.ReadOnlyField()
    update_date = serializers.ReadOnlyField()
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'comment', 'creation_date', 'update_date', 'author')


# Will re-think that part
class UpVoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    def create(self, validated_data):
        return Comment.objects.create(author=serializers.CurrentUserDefault(), **validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)

        instance.update_date = datetime.now()
        instance.save()
        return instance


class DownVoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CreateOnlyDefault(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.update_date = datetime.now()
        instance.save()
        return instance