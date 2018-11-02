from django.db import models
from api.profiles.models import User
from datetime import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(null=True)
    visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, models.SET_NULL, null=True, related_name='comment')
    body = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(null=True)
    visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True)


class UpVote(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    item = models.ForeignKey(Post, models.SET_NULL, null=True)


class DownVote(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    item = models.ForeignKey(Post, models.SET_NULL, null=True)
